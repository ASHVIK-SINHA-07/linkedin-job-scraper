-> LinkedIn Job Scraper v2.0

<!-- 🔍 **Automate your job search on LinkedIn** - Extract job listings and export to CSV in minutes.

<p align="center">
  <a href="mailto:your.email@example.com?subject=LinkedIn%20Scraper%20Customization%20Request">
    <img src="https://img.shields.io/badge/📧_Hire_Me-For_Custom_Automation-success?style=for-the-badge" alt="Hire Me">
  </a>
  <a href="https://github.com/ASHVIK-SINHA-07/linkedin-job-scraper/fork">
    <img src="https://img.shields.io/badge/🍴_Fork-This_Project-blue?style=for-the-badge" alt="Fork">
  </a>
  <a href="https://github.com/ASHVIK-SINHA-07/linkedin-job-scraper/issues">
    <img src="https://img.shields.io/badge/💡_Request-A_Feature-yellow?style=for-the-badge" alt="Feature Request">
  </a>
</p> -->

🔍 **Automate your job search on LinkedIn** - Extract job listings and export to CSV in minutes.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/ASHVIK-SINHA-07/linkedin-job-scraper?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/ASHVIK-SINHA-07/linkedin-job-scraper?style=for-the-badge" alt="Last Commit">
</p>

> 🚀 **Built by [Ashvik Sinha](https://github.com/ASHVIK-SINHA-07)**  | **[LinkedIn](https://linkedin.com/in/ashvik-sinha)**

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
  - [Windows 10/11](#windows-1011)
  - [macOS (Intel & Apple Silicon)](#macos-intel--apple-silicon)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Output Files](#-output-files)
- [Common Issues & Fixes](#-common-issues--fixes)
- [FAQ](#-faq)
- [Disclaimer](#-disclaimer)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌐 **Cross-Platform** | Works on Windows, macOS (Intel & M1/M2), and Linux |
| 📊 **Progress Bar** | Visual progress with estimated time remaining |
| ⚙️ **Configurable** | Edit `config.json` to customize behavior |
| 🔄 **Auto-Retry** | Automatic retries on network failures |
| 📝 **Logging** | Detailed logs saved to file |
| 🛡️ **Error Handling** | Clear error messages with fix suggestions |
| 🎯 **Experience Filter** | Filter by internship, entry, mid-senior, etc. |
| 📁 **Multiple Exports** | Save as CSV and/or JSON |
| 🔒 **Rate Limiting** | Respectful scraping with configurable delays |

---
## 🎥 Demo

### Terminal Output
```
============================================================
         🔗 LinkedIn Job Scraper v2.0
============================================================
🖥️  Platform: macOS 14.0
🐍 Python: 3.11.5
============================================================

📋 Enter job title (e.g., 'Python Developer'): Data Analyst
📍 Enter location (default: India): New York
🔢 How many jobs? (default: 50, max: 500): 25

Scraping jobs: |████████████████████| 25/25 (100%) [0:00:08]

✅ Successfully scraped 25 jobs
✅ CSV saved to: ~/Downloads/job_results/linkedin_jobs_Data_Analyst_New_York_2026-02-05.csv
```

### Sample Output (CSV)
| Job Title | Company | Location | Posted Date |
|-----------|---------|----------|-------------|
| Data Analyst | Google | New York, NY | 2 days ago |
| Senior Data Analyst | Meta | New York, NY | 1 week ago |
| Business Data Analyst | Amazon | Brooklyn, NY | 3 days ago |


### Terminal Output

<p align="center">
  <img src="https://github.com/ASHVIK-SINHA-07/linkedin-job-scraper/blob/main/screenshots/Screenshot-demo-1.png" alt="Terminal Screenshot" width="700">
</p>

*The scraper in action - extracting 100+ jobs with real-time progress tracking*

---

<p align="center">
  <img src="https://github.com/ASHVIK-SINHA-07/linkedin-job-scraper/blob/main/screenshots/Screenshot-demo.png" alt="CSV Screenshot" width="700">
</p>

*Clean, organized data ready for Excel or Google Sheets*

## 🚀 Quick Start

```bash
# 1. Clone or download the files
# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python linkedin_job_scraper.py
```

---

## 📥 Installation

### Windows 10/11

#### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: Check ✅ "Add Python to PATH" during installation
3. Open Command Prompt and verify:
   ```cmd
   python --version
   ```

#### Step 2: Download the Scraper

1. Download all files to a folder (e.g., `C:\Users\YourName\linkedin-scraper\`)
2. Files needed:
   - `linkedin_job_scraper.py`
   - `config.json`
   - `requirements.txt`

#### Step 3: Install Dependencies

```cmd
cd C:\Users\YourName\linkedin-scraper
pip install -r requirements.txt
```

#### Step 4: Run the Scraper

```cmd
python linkedin_job_scraper.py
```

#### Windows-Specific Notes

- If you see encoding errors, the script automatically handles UTF-8
- CSV files are saved with Excel-compatible encoding (UTF-8 BOM)
- Output folder: `Downloads\job_results\`

---

### macOS (Intel & Apple Silicon)

#### Step 1: Install Python

**Option A: Using Homebrew (Recommended)**
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**Option B: Download from python.org**
1. Download from [python.org](https://www.python.org/downloads/macos/)
2. Run the installer

#### Step 2: Download the Scraper

```bash
# Create a folder
mkdir ~/linkedin-scraper
cd ~/linkedin-scraper

# Copy the files here
```

#### Step 3: Install Dependencies

```bash
pip3 install -r requirements.txt
```

#### Step 4: Fix SSL Certificates (Important for macOS!)

```bash
# Run the certificate installer (replace 3.x with your version)
/Applications/Python\ 3.12/Install\ Certificates.command

# Or install certifi
pip3 install --upgrade certifi
```

#### Step 5: Run the Scraper

```bash
python3 linkedin_job_scraper.py
```

#### macOS-Specific Notes

- **Apple Silicon (M1/M2/M3)**: All dependencies are ARM-native compatible
- **SSL Errors**: Run the certificate command above
- Output folder: `~/Downloads/job_results/`

---

### Linux (Ubuntu/Debian)

#### Step 1: Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Step 2: Create Virtual Environment (Recommended)

```bash
mkdir ~/linkedin-scraper
cd ~/linkedin-scraper

python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Scraper

```bash
python linkedin_job_scraper.py
```

#### Linux-Specific Notes

- Make executable: `chmod +x linkedin_job_scraper.py`
- Run directly: `./linkedin_job_scraper.py`
- Output folder: `~/Downloads/job_results/`

---

## 💻 Usage

### Interactive Mode

Simply run the script and follow the prompts:

```bash
python linkedin_job_scraper.py
```

You'll be asked for:
1. **Job Title**: e.g., "Python Developer", "Data Scientist"
2. **Location**: e.g., "Bangalore, India", "New York, USA"
3. **Number of Jobs**: How many job listings to scrape (1-500)
4. **Experience Level**: Internship, Entry, Mid-Senior, etc.
5. **Export Format**: CSV only or CSV + JSON

### Example Session

```
============================================================
         🔗 LinkedIn Job Scraper v2.0
============================================================

📁 Output folder: /Users/username/Downloads/job_results
⚙️  Edit config.json to change default settings.

📋 Enter job title (e.g., 'Python Developer'): Python Developer
📍 Enter location (default: India): Bangalore
🔢 How many jobs? (default: 50, max: 500): 100
📊 Select experience level (1-7, default: 7): 2
💾 Also export as JSON? (y/n, default: n): n

⏱️  Estimated time: ~10 seconds

🚀 Start scraping? (y/n): y

🌐 Checking internet connection...
✅ Internet connection OK

Scraping jobs: |████████████████████| 100/100 (100%) [0:00:12<0:00:00]

✅ Successfully scraped 100 jobs
✅ CSV saved to: /Users/username/Downloads/job_results/linkedin_jobs_Python_Developer_Bangalore_2025-02-03_14-30-45.csv
✅ Execution time: 0 min 12 sec
```

---

## ⚙️ Configuration

Edit `config.json` to customize the scraper:

```json
{
  "default_location": "India",
  "default_num_jobs": 50,
  "max_jobs_limit": 500,
  "output_folder": "job_results",
  "delay_between_requests": 2.5,
  "max_retries": 3,
  "timeout_seconds": 30,
  "save_to_downloads": true,
  "export_json": false,
  "show_progress_bar": true,
  "log_to_file": true
}
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `default_location` | `"India"` | Default location when user presses Enter |
| `default_num_jobs` | `50` | Default number of jobs to scrape |
| `max_jobs_limit` | `500` | Maximum jobs allowed per session |
| `output_folder` | `"job_results"` | Folder name for output files |
| `delay_between_requests` | `2.5` | Seconds to wait between requests |
| `max_retries` | `3` | Number of retry attempts on failure |
| `timeout_seconds` | `30` | HTTP request timeout |
| `save_to_downloads` | `true` | Save to Downloads folder (false = script folder) |
| `export_json` | `false` | Also export JSON by default |
| `show_progress_bar` | `true` | Show progress bar during scraping |
| `log_to_file` | `true` | Save detailed log to file |

---

## 📁 Output Files

### CSV File
- **Location**: `Downloads/job_results/` (or configured folder)
- **Filename**: `linkedin_jobs_{title}_{location}_{timestamp}.csv`
- **Encoding**: UTF-8 with BOM (Excel-compatible)

### CSV Columns

| Column | Description | Example |
|--------|-------------|---------|
| Job Title | Position title | Python Developer |
| Company | Company name | Google |
| Location | Job location | Bangalore, Karnataka, India |
| URL | LinkedIn job link | https://www.linkedin.com/jobs/view/123456 |
| Posted Date | When posted | 2 days ago |

### JSON File (Optional)
- Same data in JSON format
- Useful for programmatic processing

### Log File
- **Location**: Same as output folder
- **Filename**: `scraper_log_{timestamp}.txt`
- Contains: timestamps, errors, warnings, statistics

---

## 🔧 Common Issues & Fixes

### ❌ "No module named 'requests'"

**Cause**: Dependencies not installed

**Fix**:
```bash
pip install -r requirements.txt
```

---

### ❌ SSL Certificate Error (macOS)

**Cause**: Python can't verify SSL certificates

**Fix**:
```bash
# Option 1: Run certificate installer
/Applications/Python\ 3.12/Install\ Certificates.command

# Option 2: Install certifi
pip install --upgrade certifi
```

---

### ❌ "Permission denied" when saving CSV

**Cause**: No write permission to output folder

**Fix**:
1. Edit `config.json`:
   ```json
   {
     "save_to_downloads": false,
     "output_folder": "output"
   }
   ```
2. Or run as administrator (Windows) / with sudo (Linux)

---

### ❌ LinkedIn blocked the request (403 Forbidden)

**Cause**: Too many requests or IP blocked

**Fix**:
1. Wait 5-10 minutes before trying again
2. Increase delay in `config.json`:
   ```json
   {
     "delay_between_requests": 5
   }
   ```
3. Use a VPN

---

### ❌ Rate limited (429 Error)

**Cause**: Too many requests too quickly

**Fix**:
1. Wait 10-15 minutes
2. Reduce number of jobs per session
3. Increase `delay_between_requests` to 5 seconds

---

### ❌ No jobs found

**Cause**: Could be several reasons

**Fixes**:
1. Check your internet connection
2. Try a different job title (more generic)
3. Try a different location
4. LinkedIn may have changed their HTML structure

---

### ❌ Emojis not displaying (Windows)

**Cause**: Windows Command Prompt doesn't support Unicode well

**Fix**:
1. Use Windows Terminal (recommended)
2. Or use PowerShell
3. The script tries to handle this automatically

---

### ❌ CSV shows weird characters in Excel

**Cause**: Encoding issue

**Fix**:
1. The script already uses UTF-8 BOM encoding
2. If still issues, open Excel → Data → From Text/CSV → Select UTF-8

---

## ❓ FAQ

### Q: Is this legal?

A: This script scrapes publicly available job listings from LinkedIn's guest job search. It does not require login or access any private data. However, always respect LinkedIn's Terms of Service and robots.txt. Use responsibly.

### Q: How many jobs can I scrape?

A: The default limit is 500 jobs per session. You can change `max_jobs_limit` in `config.json`, but be respectful of LinkedIn's servers.

### Q: Why are some fields "N/A"?

A: LinkedIn may not provide all information for every job listing. "N/A" indicates the data wasn't available.

### Q: Can I scrape jobs from multiple locations?

A: Not in a single run. You need to run the script multiple times with different locations.

### Q: How often does LinkedIn change their HTML structure?

A: Occasionally. If the script stops working, it may need updating to match new class names. Check for updates or report issues.

### Q: Can I use this for commercial purposes?

A: This tool is for educational and personal use. For commercial use, consider LinkedIn's official API or consult their terms of service.

---

## 🎬 Video Tutorial

*Coming Soon*

<!-- Placeholder for video tutorial link -->

---

## 📄 License

MIT License - Use freely, but respect LinkedIn's terms of service.

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. 

- Always respect LinkedIn's Terms of Service
- Use responsible scraping practices
- Don't overwhelm LinkedIn's servers
- Data scraped should be used ethically and legally
- The authors are not responsible for misuse

**LinkedIn may change their website structure at any time, which could break this scraper.**

---

## 📞 Support

If you encounter issues:

1. Check the [Common Issues](#-common-issues--fixes) section
2. Review the log file for error details
3. Open a [GitHub Issue](https://github.com/ASHVIK-SINHA-07/linkedin-job-scraper/issues) with:
   - Your OS and Python version
   - The error message
   - Steps to reproduce

---

## 🌟 Star History

If this project helped you, please consider giving it a ⭐!

---

## 👨‍💻 About the Developer

Built by **Ashvik Sinha** - BTech CSE student @ Bennett University specializing in Python automation and web scraping.


I build Python automation solutions. If you need something similar or want to collaborate:

- 📧 **Email:** [ashviksinha3001@gmail.com] 
- 🔗 **LinkedIn:** [<https://linkedin.com/in/ashvik-sinha)>] 
- 🐙 **GitHub:** [@ASHVIK-SINHA-07](https://github.com/ASHVIK-SINHA-07)

**Average Response Time:** Within 24 hours

---

Made with ❤️ for job seekers everywhere
