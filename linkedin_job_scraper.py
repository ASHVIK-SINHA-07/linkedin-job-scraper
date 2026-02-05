#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn Job Scraper - Production Ready
=======================================
A cross-platform Python script to scrape job listings from LinkedIn's public job board
and export them to CSV/JSON format.

Supported Platforms:
- Windows 10/11
- macOS (Intel and Apple Silicon)
- Linux (Ubuntu/Debian/Fedora)

LinkedIn URL Structure:
-----------------------
Base URL: https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search
Parameters:
    - keywords: Job title or search keywords (URL encoded)
    - location: City, state, or country
    - start: Pagination offset (0, 25, 50, 75, etc.)
    - Experience level filter (1=Internship, 2=Entry, 3=Associate, 4=Mid-Senior, 5=Director, 6=Executive)

DISCLAIMER:
-----------
This script is for educational purposes only. Please respect LinkedIn's terms of service
and use responsible scraping practices (rate limiting, reasonable request volumes).
"""

from __future__ import annotations

import sys
import os
import json
import re
import time
import logging
import platform
import ssl
import socket
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any
from urllib.parse import quote_plus

# =============================================================================
# CROSS-PLATFORM SETUP
# =============================================================================

def setup_platform():
    """
    Configure platform-specific settings for Windows, macOS, and Linux.
    Handles encoding issues, SSL certificates, and console output.
    """
    system = platform.system().lower()
    
    # Windows-specific fixes
    if system == 'windows':
        # Fix Windows console encoding for Unicode characters (emojis, etc.)
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except AttributeError:
            # Python < 3.7 fallback
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
        
        # Enable ANSI colors in Windows terminal
        try:
            os.system('color')
        except Exception:
            pass
    
    # macOS-specific fixes
    elif system == 'darwin':
        # Fix SSL certificate issues on macOS
        try:
            import certifi
            ssl_context = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            pass
        
        # Handle potential issues with Apple Silicon
        if platform.machine() == 'arm64':
            # M1/M2 Macs may need Rosetta for some packages
            pass
    
    # Linux-specific
    elif system == 'linux':
        # Ensure UTF-8 locale
        os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
    
    return system


# Initialize platform settings
CURRENT_PLATFORM = setup_platform()


# =============================================================================
# DEPENDENCY CHECKER
# =============================================================================

def check_dependencies() -> Tuple[bool, List[str]]:
    """
    Check if all required libraries are installed.
    
    Returns:
        Tuple[bool, List[str]]: (all_installed, list_of_missing_packages)
    """
    required_packages = {
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'pandas': 'pandas',
        'tqdm': 'tqdm',
    }
    
    optional_packages = {
        'certifi': 'certifi',  # For SSL certificate handling on macOS
    }
    
    missing_required = []
    missing_optional = []
    
    # Check required packages
    for import_name, pip_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_required.append(pip_name)
    
    # Check optional packages
    for import_name, pip_name in optional_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_optional.append(pip_name)
    
    if missing_required:
        print("\n" + "=" * 60)
        print("❌ MISSING REQUIRED DEPENDENCIES")
        print("=" * 60)
        print("\nThe following required libraries are not installed:\n")
        for pkg in missing_required:
            print(f"  • {pkg}")
        print("\n📦 Install them with the following command:\n")
        print(f"    pip install {' '.join(missing_required)}")
        print("\nOr install all dependencies at once:")
        print("    pip install -r requirements.txt")
        print("\n" + "=" * 60)
        return False, missing_required
    
    if missing_optional:
        print(f"\n⚠️  Optional packages not installed: {', '.join(missing_optional)}")
        print("   These are recommended but not required.\n")
    
    return True, []


# Check dependencies before importing
deps_ok, missing = check_dependencies()
if not deps_ok:
    print("\n❌ Please install the missing dependencies and try again.")
    sys.exit(1)

# Now import the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

try:
    import certifi
    SSL_CERT_FILE = certifi.where()
except ImportError:
    SSL_CERT_FILE = None


# =============================================================================
# CONFIGURATION MANAGEMENT
# =============================================================================

class Config:
    """
    Configuration manager for the LinkedIn Job Scraper.
    Handles loading, saving, and creating default configuration.
    """
    
    DEFAULT_CONFIG = {
        "default_location": "India",
        "default_num_jobs": 50,
        "max_jobs_limit": 500,
        "output_folder": "job_results",
        "delay_between_requests": 2.5,
        "max_retries": 3,
        "timeout_seconds": 30,
        "save_to_downloads": True,
        "export_json": False,
        "show_progress_bar": True,
        "log_to_file": True,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize configuration manager.
        
        Args:
            config_path: Path to config.json file. If None, uses script directory.
        """
        if config_path is None:
            self.config_path = Path(__file__).parent / "config.json"
        else:
            self.config_path = Path(config_path)
        
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                # Merge with defaults (user config overrides defaults)
                config = {**self.DEFAULT_CONFIG, **user_config}
                return config
            except json.JSONDecodeError as e:
                print(f"⚠️  Error reading config.json: {e}")
                print("   Using default configuration.")
                return self.DEFAULT_CONFIG.copy()
            except PermissionError:
                print(f"⚠️  Permission denied reading config.json")
                print("   Using default configuration.")
                return self.DEFAULT_CONFIG.copy()
        else:
            # Create default config file
            self._save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()
    
    def _save_config(self, config: Dict[str, Any]) -> bool:
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"⚠️  Permission denied writing to {self.config_path}")
            return False
        except Exception as e:
            print(f"⚠️  Error saving config: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self.config[key] = value
    
    def save(self) -> bool:
        """Save current configuration to file."""
        return self._save_config(self.config)


# =============================================================================
# LOGGING SETUP
# =============================================================================

class Logger:
    """
    Logger for tracking scraping activities and errors.
    Writes to both console and log file.
    """
    
    def __init__(self, output_dir: Path, enabled: bool = True):
        """
        Initialize logger.
        
        Args:
            output_dir: Directory to save log file
            enabled: Whether to write logs to file
        """
        self.enabled = enabled
        self.output_dir = output_dir
        self.log_entries = []
        self.start_time = datetime.now()
        
        if enabled:
            self.log_file = output_dir / f"scraper_log_{self.start_time.strftime('%Y%m%d_%H%M%S')}.txt"
        else:
            self.log_file = None
    
    def log(self, message: str, level: str = "INFO") -> None:
        """Log a message."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self.log_entries.append(entry)
        
        if self.enabled and self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(entry + "\n")
            except Exception:
                pass  # Silently fail if can't write to log
    
    def info(self, message: str) -> None:
        """Log info message."""
        self.log(message, "INFO")
    
    def error(self, message: str) -> None:
        """Log error message."""
        self.log(message, "ERROR")
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        self.log(message, "WARNING")
    
    def get_summary(self) -> str:
        """Get execution summary."""
        elapsed = datetime.now() - self.start_time
        minutes = int(elapsed.total_seconds() // 60)
        seconds = int(elapsed.total_seconds() % 60)
        return f"{minutes} min {seconds} sec"


# =============================================================================
# PATH UTILITIES
# =============================================================================

class PathManager:
    """
    Cross-platform path management for file operations.
    """
    
    @staticmethod
    def get_downloads_folder() -> Path:
        """
        Get the user's Downloads folder path based on the OS.
        
        Returns:
            Path: Path to Downloads folder
        """
        system = platform.system().lower()
        
        if system == 'windows':
            # Try known Windows paths
            downloads = Path.home() / "Downloads"
            if not downloads.exists():
                # Fallback to OneDrive Downloads if exists
                onedrive_downloads = Path.home() / "OneDrive" / "Downloads"
                if onedrive_downloads.exists():
                    return onedrive_downloads
        elif system == 'darwin':  # macOS
            downloads = Path.home() / "Downloads"
        else:  # Linux and others
            # Check XDG user directories
            xdg_download = os.environ.get('XDG_DOWNLOAD_DIR')
            if xdg_download:
                downloads = Path(xdg_download)
            else:
                downloads = Path.home() / "Downloads"
        
        # Fallback to home directory if Downloads doesn't exist
        if not downloads.exists():
            downloads = Path.home()
        
        return downloads
    
    @staticmethod
    def get_output_folder(config: Config) -> Path:
        """
        Get the output folder based on configuration.
        
        Args:
            config: Configuration object
            
        Returns:
            Path: Path to output folder
        """
        if config.get('save_to_downloads', True):
            base = PathManager.get_downloads_folder()
        else:
            base = Path(__file__).parent
        
        output_folder = base / config.get('output_folder', 'job_results')
        
        # Create folder if it doesn't exist
        try:
            output_folder.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            print(f"⚠️  Cannot create folder: {output_folder}")
            print("   Falling back to current directory.")
            output_folder = Path.cwd()
        
        return output_folder
    
    @staticmethod
    def sanitize_filename(name: str) -> str:
        """
        Sanitize a string to be safe for use as a filename.
        
        Args:
            name: Original string
            
        Returns:
            str: Sanitized filename-safe string
        """
        # Remove or replace invalid characters
        # Windows: \ / : * ? " < > |
        # macOS/Linux: / and null
        invalid_chars = r'[\\/:*?"<>|\x00]'
        sanitized = re.sub(invalid_chars, '_', name)
        # Remove leading/trailing spaces and dots
        sanitized = sanitized.strip(' .')
        # Limit length
        if len(sanitized) > 50:
            sanitized = sanitized[:50]
        return sanitized if sanitized else "untitled"
    
    @staticmethod
    def generate_output_filename(job_title: str, location: str, extension: str = "csv") -> str:
        """
        Generate a timestamped output filename.
        
        Args:
            job_title: Job title searched
            location: Location searched
            extension: File extension (csv, json, txt)
            
        Returns:
            str: Generated filename
        """
        safe_title = PathManager.sanitize_filename(job_title)
        safe_location = PathManager.sanitize_filename(location)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"linkedin_jobs_{safe_title}_{safe_location}_{timestamp}.{extension}"


# =============================================================================
# NETWORK UTILITIES
# =============================================================================

class NetworkManager:
    """
    Network utilities for handling HTTP requests with proper error handling.
    """
    
    def __init__(self, config: Config, logger: Logger):
        """
        Initialize network manager.
        
        Args:
            config: Configuration object
            logger: Logger instance
        """
        self.config = config
        self.logger = logger
        self.session = requests.Session()
        
        # Set up session with default headers
        self.session.headers.update({
            "User-Agent": config.get('user_agent'),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        })
        
        # SSL certificate verification
        if SSL_CERT_FILE:
            self.session.verify = SSL_CERT_FILE
    
    def check_internet_connection(self) -> bool:
        """
        Check if there's an active internet connection.
        
        Returns:
            bool: True if connected, False otherwise
        """
        try:
            # Try to connect to multiple reliable hosts
            hosts = [
                ("8.8.8.8", 53),      # Google DNS
                ("1.1.1.1", 53),       # Cloudflare DNS
                ("208.67.222.222", 53) # OpenDNS
            ]
            for host, port in hosts:
                try:
                    socket.create_connection((host, port), timeout=3)
                    return True
                except (socket.timeout, socket.error):
                    continue
            return False
        except Exception:
            return False
    
    def fetch_page(self, url: str, params: Dict[str, Any]) -> Optional[str]:
        """
        Fetch a page with proper error handling and retries.
        
        Args:
            url: URL to fetch
            params: URL parameters
            
        Returns:
            Optional[str]: HTML content or None if failed
        """
        max_retries = self.config.get('max_retries', 3)
        timeout = self.config.get('timeout_seconds', 30)
        
        for attempt in range(max_retries):
            try:
                response = self.session.get(url, params=params, timeout=timeout)
                response.raise_for_status()
                
                if response.status_code == 200:
                    return response.text
                else:
                    self.logger.warning(f"Received status code: {response.status_code}")
                    return None
                    
            except requests.exceptions.Timeout:
                self.logger.warning(f"Request timed out (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(2)
                continue
                
            except requests.exceptions.ConnectionError:
                self.logger.error("Connection error - no internet or DNS failure")
                if not self.check_internet_connection():
                    raise ConnectionError(
                        "No internet connection detected.\n"
                        "Please check your network connection and try again."
                    )
                if attempt < max_retries - 1:
                    time.sleep(2)
                continue
                
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code if e.response else None
                if status_code == 429:
                    self.logger.error("Rate limited by LinkedIn (429)")
                    raise RateLimitError(
                        "LinkedIn has rate-limited your requests.\n"
                        "Please wait 5-10 minutes before trying again.\n"
                        "Tip: Reduce the number of jobs or increase delay between requests."
                    )
                elif status_code == 403:
                    self.logger.error("Access forbidden by LinkedIn (403)")
                    raise AccessBlockedError(
                        "LinkedIn has blocked your request (403 Forbidden).\n"
                        "This may be due to:\n"
                        "  • Too many requests in a short time\n"
                        "  • Your IP has been temporarily blocked\n"
                        "Try again later or use a VPN."
                    )
                else:
                    self.logger.error(f"HTTP Error: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                    continue
                    
            except requests.exceptions.SSLError as e:
                self.logger.error(f"SSL Error: {e}")
                raise SSLError(
                    "SSL Certificate verification failed.\n"
                    "This can happen on macOS. Try:\n"
                    "  1. Run: pip install --upgrade certifi\n"
                    "  2. Run: /Applications/Python 3.x/Install Certificates.command"
                )
                
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Request failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                continue
        
        return None


# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

class ScraperError(Exception):
    """Base exception for scraper errors."""
    pass

class RateLimitError(ScraperError):
    """Raised when LinkedIn rate-limits requests."""
    pass

class AccessBlockedError(ScraperError):
    """Raised when LinkedIn blocks access."""
    pass

class SSLError(ScraperError):
    """Raised when SSL certificate verification fails."""
    pass

class InputValidationError(ScraperError):
    """Raised when user input is invalid."""
    pass


# =============================================================================
# CONSTANTS
# =============================================================================

BASE_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
JOBS_PER_PAGE = 25

EXPERIENCE_LEVELS = {
    "internship": "1",
    "entry": "2",
    "associate": "3",
    "mid-senior": "4",
    "director": "5",
    "executive": "6"
}


# =============================================================================
# JOB SCRAPER CLASS
# =============================================================================

class LinkedInJobScraper:
    """
    Main LinkedIn Job Scraper class.
    Handles scraping, parsing, and exporting job listings.
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the scraper.
        
        Args:
            config: Configuration object. If None, creates default config.
        """
        self.config = config or Config()
        self.output_dir = PathManager.get_output_folder(self.config)
        self.logger = Logger(self.output_dir, self.config.get('log_to_file', True))
        self.network = NetworkManager(self.config, self.logger)
        self.jobs: List[Dict[str, str]] = []
    
    def fetch_job_page(
        self,
        keywords: str,
        location: str,
        start: int = 0,
        experience_level: Optional[str] = None
    ) -> Optional[str]:
        """
        Fetch a page of job listings from LinkedIn.
        
        Args:
            keywords: Job title or search keywords
            location: Location to search in
            start: Pagination offset
            experience_level: Optional experience level filter
            
        Returns:
            Optional[str]: HTML content or None if failed
        """
        params = {
            "keywords": keywords,
            "location": location,
            "start": start,
        }
        
        if experience_level and experience_level.lower() in EXPERIENCE_LEVELS:
            params["f_E"] = EXPERIENCE_LEVELS[experience_level.lower()]
        
        return self.network.fetch_page(BASE_URL, params)
    
    def parse_jobs(self, html_content: str) -> List[Dict[str, str]]:
        """
        Parse job listings from HTML content.
        
        Args:
            html_content: Raw HTML from LinkedIn
            
        Returns:
            List of job dictionaries
        """
        if not html_content:
            return []
        
        jobs = []
        soup = BeautifulSoup(html_content, 'html.parser')
        job_cards = soup.find_all('li')
        
        for card in job_cards:
            try:
                job_data = self._parse_job_card(card)
                if job_data:
                    jobs.append(job_data)
            except Exception as e:
                self.logger.warning(f"Error parsing job card: {e}")
                continue
        
        return jobs
    
    def _parse_job_card(self, card) -> Optional[Dict[str, str]]:
        """
        Parse a single job card.
        
        Args:
            card: BeautifulSoup element representing a job card
            
        Returns:
            Job dictionary or None if parsing fails
        """
        job_data = {}
        
        # Extract Job Title
        title_elem = (
            card.find('h3', class_='base-search-card__title') or
            card.find('h3', {'class': lambda x: x and 'title' in x.lower() if x else False}) or
            card.find('h3') or
            card.find('a', class_='base-card__full-link')
        )
        job_data['job_title'] = self._clean_text(title_elem.get_text()) if title_elem else "N/A"
        
        if job_data['job_title'] == "N/A" or len(job_data['job_title']) < 2:
            return None
        
        # Extract Company Name
        company_elem = (
            card.find('h4', class_='base-search-card__subtitle') or
            card.find('a', class_='hidden-nested-link') or
            card.find('h4') or
            card.find('a', {'class': lambda x: x and 'company' in x.lower() if x else False})
        )
        job_data['company'] = self._clean_text(company_elem.get_text()) if company_elem else "N/A"
        
        # Extract Location
        location_elem = (
            card.find('span', class_='job-search-card__location') or
            card.find('span', {'class': lambda x: x and 'location' in x.lower() if x else False}) or
            card.find('span', class_='base-search-card__metadata')
        )
        job_data['location'] = self._clean_text(location_elem.get_text()) if location_elem else "N/A"
        
        # Extract Job URL
        url_elem = (
            card.find('a', class_='base-card__full-link') or
            card.find('a', href=lambda x: x and '/jobs/view/' in x if x else False) or
            card.find('a', href=True)
        )
        if url_elem and url_elem.get('href'):
            job_url = url_elem['href']
            if job_url.startswith('/'):
                job_url = f"https://www.linkedin.com{job_url}"
            elif not job_url.startswith('http'):
                job_url = f"https://www.linkedin.com/{job_url}"
            job_data['url'] = job_url.split('?')[0] if '?' in job_url else job_url
        else:
            job_data['url'] = "N/A"
        
        # Extract Posted Date
        date_elem = (
            card.find('time', class_='job-search-card__listdate') or
            card.find('time', class_='job-search-card__listdate--new') or
            card.find('time') or
            card.find('span', {'class': lambda x: x and 'date' in x.lower() if x else False})
        )
        if date_elem:
            job_data['posted_date'] = date_elem.get('datetime') or self._clean_text(date_elem.get_text())
        else:
            job_data['posted_date'] = "N/A"
        
        if job_data['job_title'] != "N/A" and job_data['url'] != "N/A":
            return job_data
        return None
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if not text:
            return "N/A"
        cleaned = ' '.join(text.split())
        return cleaned.strip() if cleaned else "N/A"
    
    def _deduplicate_jobs(self, jobs: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Remove duplicate job listings."""
        seen_urls = set()
        unique_jobs = []
        
        for job in jobs:
            url = job.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_jobs.append(job)
        
        return unique_jobs
    
    def scrape(
        self,
        job_title: str,
        location: str,
        num_jobs: int = 50,
        experience_level: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """
        Main scraping function with progress bar.
        
        Args:
            job_title: Job title to search for
            location: Location to search in
            num_jobs: Target number of jobs
            experience_level: Optional experience filter
            
        Returns:
            List of job dictionaries
        """
        self.logger.info(f"Starting scrape: '{job_title}' in '{location}', target: {num_jobs}")
        
        all_jobs = []
        start = 0
        consecutive_empty = 0
        max_consecutive_empty = 3
        delay = self.config.get('delay_between_requests', 2.5)
        
        # Calculate estimated pages
        estimated_pages = (num_jobs + JOBS_PER_PAGE - 1) // JOBS_PER_PAGE
        
        # Create progress bar
        use_progress_bar = self.config.get('show_progress_bar', True)
        
        if use_progress_bar:
            pbar = tqdm(
                total=num_jobs,
                desc="Scraping jobs",
                unit="jobs",
                bar_format="{desc}: {bar}| {n_fmt}/{total_fmt} ({percentage:.0f}%) [{elapsed}<{remaining}]"
            )
        
        try:
            while len(all_jobs) < num_jobs:
                # Update progress bar description
                if use_progress_bar:
                    pbar.set_description(f"Fetching page {(start // JOBS_PER_PAGE) + 1}")
                
                # Fetch page
                html_content = self.fetch_job_page(job_title, location, start, experience_level)
                
                if html_content is None:
                    consecutive_empty += 1
                    if consecutive_empty >= max_consecutive_empty:
                        self.logger.warning(f"Stopping: {max_consecutive_empty} consecutive failed requests")
                        break
                    time.sleep(delay * 2)
                    continue
                
                # Parse jobs
                if use_progress_bar:
                    pbar.set_description("Parsing jobs")
                
                page_jobs = self.parse_jobs(html_content)
                
                if not page_jobs:
                    consecutive_empty += 1
                    if consecutive_empty >= max_consecutive_empty:
                        self.logger.info("No more jobs found")
                        break
                else:
                    consecutive_empty = 0
                    all_jobs.extend(page_jobs)
                    
                    if use_progress_bar:
                        pbar.update(len(page_jobs))
                    
                    self.logger.info(f"Found {len(page_jobs)} jobs on page {(start // JOBS_PER_PAGE) + 1}")
                
                start += JOBS_PER_PAGE
                
                if len(all_jobs) >= num_jobs:
                    break
                
                # Rate limiting
                if use_progress_bar:
                    pbar.set_description(f"Waiting {delay}s")
                time.sleep(delay)
        
        finally:
            if use_progress_bar:
                pbar.close()
        
        # Deduplicate
        original_count = len(all_jobs)
        all_jobs = self._deduplicate_jobs(all_jobs)
        if len(all_jobs) < original_count:
            self.logger.info(f"Removed {original_count - len(all_jobs)} duplicates")
        
        # Trim to requested number
        if len(all_jobs) > num_jobs:
            all_jobs = all_jobs[:num_jobs]
        
        self.jobs = all_jobs
        self.logger.info(f"Scraping complete: {len(all_jobs)} jobs found")
        
        return all_jobs
    
    def export_to_csv(self, job_title: str, location: str) -> Optional[Path]:
        """
        Export jobs to CSV file.
        
        Args:
            job_title: Job title (for filename)
            location: Location (for filename)
            
        Returns:
            Path to CSV file or None if failed
        """
        if not self.jobs:
            self.logger.warning("No jobs to export")
            return None
        
        filename = PathManager.generate_output_filename(job_title, location, "csv")
        filepath = self.output_dir / filename
        
        try:
            df = pd.DataFrame(self.jobs)
            df.columns = ['Job Title', 'Company', 'Location', 'URL', 'Posted Date']
            
            # Use utf-8-sig for Excel compatibility on Windows
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            
            self.logger.info(f"CSV exported: {filepath}")
            return filepath
            
        except PermissionError:
            self.logger.error(f"Permission denied writing to: {filepath}")
            print(f"\n❌ Permission Error: Cannot write to {filepath}")
            print("   Try running the script as administrator or choose a different output folder.")
            
            # Try fallback to current directory
            fallback_path = Path.cwd() / filename
            try:
                df.to_csv(fallback_path, index=False, encoding='utf-8-sig')
                self.logger.info(f"CSV exported to fallback: {fallback_path}")
                return fallback_path
            except Exception:
                return None
                
        except Exception as e:
            self.logger.error(f"Error exporting CSV: {e}")
            return None
    
    def export_to_json(self, job_title: str, location: str) -> Optional[Path]:
        """
        Export jobs to JSON file.
        
        Args:
            job_title: Job title (for filename)
            location: Location (for filename)
            
        Returns:
            Path to JSON file or None if failed
        """
        if not self.jobs:
            self.logger.warning("No jobs to export")
            return None
        
        filename = PathManager.generate_output_filename(job_title, location, "json")
        filepath = self.output_dir / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.jobs, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"JSON exported: {filepath}")
            return filepath
            
        except PermissionError:
            self.logger.error(f"Permission denied writing to: {filepath}")
            return None
        except Exception as e:
            self.logger.error(f"Error exporting JSON: {e}")
            return None
    
    def print_sample(self, num_samples: int = 5) -> None:
        """Print a sample of scraped jobs."""
        if not self.jobs:
            return
        
        print(f"\n📋 Sample of scraped jobs (showing {min(num_samples, len(self.jobs))} of {len(self.jobs)}):")
        print("=" * 80)
        
        for i, job in enumerate(self.jobs[:num_samples], 1):
            print(f"\n{i}. {job['job_title']}")
            print(f"   🏢 Company: {job['company']}")
            print(f"   📍 Location: {job['location']}")
            print(f"   📅 Posted: {job['posted_date']}")
            url = job['url']
            print(f"   🔗 URL: {url[:60]}..." if len(url) > 60 else f"   🔗 URL: {url}")
        
        print("\n" + "=" * 80)
    
    def get_summary(self) -> str:
        """Get execution summary."""
        return self.logger.get_summary()


# =============================================================================
# USER INPUT HANDLING
# =============================================================================

def validate_job_count(value: str, max_limit: int = 500) -> int:
    """
    Validate and convert job count input.
    
    Args:
        value: User input string
        max_limit: Maximum allowed jobs
        
    Returns:
        int: Validated job count
        
    Raises:
        InputValidationError: If input is invalid
    """
    if not value.strip():
        return 50  # Default
    
    try:
        num = int(value)
    except ValueError:
        raise InputValidationError(
            f"Invalid input: '{value}' is not a number.\n"
            "Please enter a positive integer (e.g., 50, 100)."
        )
    
    if num <= 0:
        raise InputValidationError(
            f"Invalid input: {num} is not positive.\n"
            "Please enter a number greater than 0."
        )
    
    if num > max_limit:
        raise InputValidationError(
            f"Invalid input: {num} exceeds maximum limit of {max_limit}.\n"
            f"Please enter a number between 1 and {max_limit}."
        )
    
    return num


def get_user_input(config: Config) -> Tuple[str, str, int, Optional[str], bool]:
    """
    Get search parameters from user with validation.
    
    Args:
        config: Configuration object
        
    Returns:
        Tuple of (job_title, location, num_jobs, experience_level, export_json)
    """
    print("\n" + "=" * 60)
    print("         🔗 LinkedIn Job Scraper v2.0")
    print("=" * 60)
    print(f"\n📁 Output folder: {PathManager.get_output_folder(config)}")
    print("⚙️  Edit config.json to change default settings.\n")
    
    # Get job title
    job_title = input("📋 Enter job title (e.g., 'Python Developer'): ").strip()
    while not job_title:
        print("⚠️  Job title cannot be empty.")
        job_title = input("📋 Enter job title: ").strip()
    
    # Get location
    default_location = config.get('default_location', 'India')
    location = input(f"📍 Enter location (default: {default_location}): ").strip()
    if not location:
        location = default_location
    
    # Get number of jobs
    default_num = config.get('default_num_jobs', 50)
    max_limit = config.get('max_jobs_limit', 500)
    
    while True:
        num_input = input(f"🔢 How many jobs? (default: {default_num}, max: {max_limit}): ").strip()
        try:
            num_jobs = validate_job_count(num_input, max_limit)
            break
        except InputValidationError as e:
            print(f"⚠️  {e}")
    
    # Get experience level
    print("\n📊 Experience level options:")
    print("   1. Internship")
    print("   2. Entry level")
    print("   3. Associate")
    print("   4. Mid-Senior level")
    print("   5. Director")
    print("   6. Executive")
    print("   7. All levels (no filter)")
    
    exp_input = input("📊 Select experience level (1-7, default: 7): ").strip()
    experience_map = {
        '1': 'internship', '2': 'entry', '3': 'associate',
        '4': 'mid-senior', '5': 'director', '6': 'executive',
        '7': None, '': None
    }
    experience_level = experience_map.get(exp_input, None)
    
    # Ask about JSON export
    default_json = config.get('export_json', False)
    json_prompt = f"💾 Also export as JSON? (y/n, default: {'y' if default_json else 'n'}): "
    export_json_input = input(json_prompt).strip().lower()
    if export_json_input == '':
        export_json = default_json
    else:
        export_json = export_json_input == 'y'
    
    return job_title, location, num_jobs, experience_level, export_json


def estimate_time(num_jobs: int, delay: float) -> str:
    """Estimate scraping time."""
    num_pages = (num_jobs + JOBS_PER_PAGE - 1) // JOBS_PER_PAGE
    total_seconds = num_pages * delay
    
    if total_seconds < 60:
        return f"~{int(total_seconds)} seconds"
    else:
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        return f"~{minutes} min {seconds} sec"


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main execution function."""
    print("\n" + "=" * 60)
    print(f"🖥️  Platform: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {platform.python_version()}")
    print("=" * 60)
    
    try:
        # Load configuration
        config = Config()
        
        # Get user input
        job_title, location, num_jobs, experience_level, export_json = get_user_input(config)
        
        # Estimate time
        delay = config.get('delay_between_requests', 2.5)
        est_time = estimate_time(num_jobs, delay)
        print(f"\n⏱️  Estimated time: {est_time}")
        
        # Confirm
        confirm = input("\n🚀 Start scraping? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Scraping cancelled.")
            return
        
        # Initialize scraper
        scraper = LinkedInJobScraper(config)
        
        # Check internet connection
        print("\n🌐 Checking internet connection...")
        if not scraper.network.check_internet_connection():
            print("❌ No internet connection detected.")
            print("   Please check your network and try again.")
            return
        print("✅ Internet connection OK\n")
        
        # Start scraping
        jobs = scraper.scrape(job_title, location, num_jobs, experience_level)
        
        if jobs:
            # Print sample
            scraper.print_sample()
            
            # Export to CSV
            csv_path = scraper.export_to_csv(job_title, location)
            
            # Export to JSON if requested
            json_path = None
            if export_json:
                json_path = scraper.export_to_json(job_title, location)
            
            # Print summary
            print("\n" + "=" * 60)
            print("                    📊 SUMMARY")
            print("=" * 60)
            print(f"\n✅ Successfully scraped {len(jobs)} jobs")
            if csv_path:
                print(f"✅ CSV saved to: {csv_path}")
            if json_path:
                print(f"✅ JSON saved to: {json_path}")
            print(f"✅ Execution time: {scraper.get_summary()}")
            print(f"✅ Search: '{job_title}' in '{location}'")
            
            if config.get('log_to_file', True):
                print(f"\n📝 Log file saved to: {scraper.logger.log_file}")
            
        else:
            print("\n⚠️  No jobs were found. This could be because:")
            print("   • LinkedIn changed their HTML structure")
            print("   • The search query returned no results")
            print("   • LinkedIn blocked the request")
            print("   Try a different job title or location.")
        
        print("\n👋 Thank you for using LinkedIn Job Scraper!")
        print("=" * 60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n❌ Scraping interrupted by user.")
        
    except RateLimitError as e:
        print(f"\n🚫 Rate Limit Error:\n{e}")
        
    except AccessBlockedError as e:
        print(f"\n🚫 Access Blocked:\n{e}")
        
    except ConnectionError as e:
        print(f"\n🔌 Connection Error:\n{e}")
        
    except SSLError as e:
        print(f"\n🔒 SSL Error:\n{e}")
        
    except InputValidationError as e:
        print(f"\n⚠️  Input Error:\n{e}")
        
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("\nIf this persists, please check:")
        print("   • Your internet connection")
        print("   • That LinkedIn hasn't changed their website structure")
        print("   • The config.json file is valid JSON")
        raise


if __name__ == "__main__":
    main()
