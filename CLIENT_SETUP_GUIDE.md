# LinkedIn Job Scraper - Setup Guide

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.11+-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey)
![Setup Time](https://img.shields.io/badge/setup%20time-5--10%20minutes-green)

**Transform your job search with automated LinkedIn scraping**

</div>

---

## 👋 Welcome!

Congratulations on taking the first step toward **automating your job search**!

This guide will walk you through setting up the LinkedIn Job Scraper on your computer. In just **5-10 minutes**, you'll have a powerful tool that can:

- ✅ Search hundreds of LinkedIn jobs in minutes
- ✅ Export everything to a neat spreadsheet (CSV)
- ✅ Filter by experience level, location, and keywords
- ✅ Run anytime with a single click

**No coding experience required!** Just follow the steps below for your operating system.

> 💡 **Pro Tip**: Keep this guide open in another window while you follow along. Copy-paste the commands to avoid typos!

---

## 📋 Table of Contents

1. [Windows Setup](#-section-1-windows-setup-windows-1011)
2. [Mac Setup](#-section-2-mac-setup-macos-monterey-ventura-sonoma)
3. [First Run Walkthrough](#-section-3-first-run-walkthrough)
4. [Customization](#-section-4-customization)
5. [FAQ](#-section-5-faq)
6. [Getting Help](#-section-6-getting-help)
7. [Video Tutorial](#-section-7-video-tutorial)

---

# 🪟 SECTION 1: Windows Setup (Windows 10/11)

## Step 1: Install Python

Python is the programming language that powers this script. Don't worry—you won't need to write any code!

### 1.1 Download Python

1. Open your web browser and go to: **[python.org/downloads](https://www.python.org/downloads/)**

2. Click the big yellow button that says **"Download Python 3.11.x"** (or the latest version)

   ```
   ┌─────────────────────────────────────┐
   │  Download Python 3.11.9             │
   │  [====== Download Button ======]    │
   └─────────────────────────────────────┘
   ```

3. Save the installer to your Downloads folder

### 1.2 Run the Installer

1. Double-click the downloaded file (e.g., `python-3.11.9-amd64.exe`)

2. **⚠️ CRITICAL STEP**: Check the box that says **"Add Python to PATH"**

   ```
   ┌────────────────────────────────────────────────────────┐
   │  Install Python 3.11.9                                 │
   │                                                        │
   │  ☑️ Install launcher for all users (recommended)       │
   │  ☑️ Add Python 3.11 to PATH  ← CHECK THIS BOX!        │
   │                                                        │
   │  [Install Now]    [Customize installation]             │
   └────────────────────────────────────────────────────────┘
   ```

   > ⚠️ **Don't skip this!** If you forget to check this box, the script won't work and you'll need to reinstall Python.

3. Click **"Install Now"**

4. Wait for installation to complete (1-2 minutes)

5. Click **"Close"** when finished

### 1.3 Verify Installation

Let's make sure Python installed correctly:

1. Press `Windows Key + R` on your keyboard
2. Type `cmd` and press Enter (this opens Command Prompt)
3. Type the following command and press Enter:

   ```cmd
   python --version
   ```

4. You should see something like:

   ```
   Python 3.11.9
   ```

   ✅ **Success!** Python is installed correctly.

   ❌ If you see `'python' is not recognized...`, go back and reinstall Python, making sure to check "Add Python to PATH"

---

## Step 2: Download the Script

### Option A: Download ZIP from GitHub (Easiest)

1. Go to the GitHub repository page for this project
2. Click the green **"Code"** button
3. Click **"Download ZIP"**

   ```
   ┌──────────────────────┐
   │  < > Code  ▼         │
   ├──────────────────────┤
   │  📋 Clone            │
   │  ────────────        │
   │  📥 Download ZIP  ←  │
   └──────────────────────┘
   ```

4. Open your **Downloads** folder
5. Right-click the ZIP file → **"Extract All..."**
6. Choose where to extract:
   - **Recommended**: `C:\Users\YourName\Documents\linkedin-job-scraper`
   - Or: `C:\Users\YourName\Desktop\linkedin-job-scraper`

### Option B: Use Git (If You Have It)

If you're familiar with Git, open Command Prompt and run:

```cmd
cd C:\Users\YourName\Documents
git clone https://github.com/your-repo/linkedin-job-scraper.git
```

---

## Step 3: Install Required Libraries

The script needs some helper libraries to work. Let's install them!

### 3.1 Open Command Prompt

1. Press `Windows Key + R`
2. Type `cmd` and press Enter

### 3.2 Navigate to the Script Folder

Type the following command (replace `YourName` with your actual Windows username):

```cmd
cd C:\Users\YourName\Documents\linkedin-job-scraper
```

> 💡 **Tip**: If you extracted to Desktop, use:
> ```cmd
> cd C:\Users\YourName\Desktop\linkedin-job-scraper
> ```

### 3.3 Install Dependencies

Copy and paste this command, then press Enter:

```cmd
pip install -r requirements.txt
```

### 3.4 What Success Looks Like

You should see output similar to this:

```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
Collecting pandas
  Downloading pandas-2.0.3-cp311-cp311-win_amd64.whl (10.6 MB)
Collecting tqdm
  Downloading tqdm-4.66.1-py3-none-any.whl (78 kB)
Successfully installed beautifulsoup4-4.12.2 pandas-2.0.3 requests-2.31.0 tqdm-4.66.1
```

✅ **Success!** All libraries are installed.

### 3.5 Common Error: "pip is not recognized"

If you see this error:
```
'pip' is not recognized as an internal or external command
```

**Solution**: Python wasn't added to PATH. Try this command instead:

```cmd
python -m pip install -r requirements.txt
```

If that still doesn't work, reinstall Python and **make sure to check "Add Python to PATH"**.

---

## Step 4: Run the Script

The exciting part—let's scrape some jobs!

### 4.1 Start the Script

In Command Prompt (still in the script folder), type:

```cmd
python linkedin_job_scraper.py
```

### 4.2 Follow the Prompts

You'll see an interactive menu:

```
============================================================
         🔗 LinkedIn Job Scraper v2.0
============================================================

📁 Output folder: C:\Users\YourName\Downloads\job_results
⚙️  Edit config.json to change default settings.

📋 Enter job title (e.g., 'Python Developer'): 
```

Enter your search criteria when prompted:
- **Job title**: e.g., `Product Manager`, `Software Engineer`, `Data Analyst`
- **Location**: e.g., `New York`, `Remote`, `San Francisco, CA`
- **Number of jobs**: e.g., `50`, `100` (start small for your first run!)
- **Experience level**: Choose 1-7 or press Enter for all levels
- **Export JSON**: Type `n` (just CSV is fine for most people)

### 4.3 Watch It Work!

You'll see a progress bar:

```
🚀 Starting LinkedIn job scraper...
🌐 Checking internet connection...
✅ Internet connection OK

Scraping jobs: |████████████████████| 50/50 (100%) [0:00:45<0:00:00]

✅ Successfully scraped 47 jobs
✅ CSV saved to: C:\Users\YourName\Downloads\job_results\linkedin_jobs_Product_Manager_New_York_20260203_143052.csv
```

### 4.4 Find Your CSV File

1. Open **File Explorer** (`Windows Key + E`)
2. Navigate to: `Downloads` → `job_results`
3. Look for a file named like: `linkedin_jobs_Product_Manager_New_York_20260203_143052.csv`

   ```
   📁 Downloads
    └── 📁 job_results
         └── 📄 linkedin_jobs_Product_Manager_New_York_20260203_143052.csv
   ```

4. Double-click to open in Excel, or right-click → "Open with" → Google Sheets

---

## Step 5: Optional - Create Desktop Shortcut

Want to run the scraper with a single double-click? Let's create a shortcut!

### 5.1 Create a Batch File

1. Right-click on your Desktop
2. Select **New** → **Text Document**
3. Name it `Run Job Scraper.txt`
4. Open it with Notepad and paste:

   ```batch
   @echo off
   cd C:\Users\YourName\Documents\linkedin-job-scraper
   python linkedin_job_scraper.py
   pause
   ```

   > ⚠️ **Important**: Replace `YourName` with your actual Windows username!

5. Save the file
6. Rename it from `Run Job Scraper.txt` to `Run Job Scraper.bat`
   - When Windows asks about changing the extension, click **Yes**

### 5.2 Using Your Shortcut

Now you can:
1. Double-click `Run Job Scraper.bat` on your Desktop
2. The scraper will start automatically!
3. The window will stay open after finishing (thanks to `pause`)

---

## 🔧 Troubleshooting Windows

### ❌ SSL Certificate Error

**Error**: `SSLError: certificate verify failed`

**Solution**:
```cmd
pip install --upgrade certifi
```

Then try running the script again.

---

### ❌ ModuleNotFoundError: No module named 'requests'

**Error**: `ModuleNotFoundError: No module named 'requests'`

**Solution**: Dependencies weren't installed. Run:
```cmd
pip install -r requirements.txt
```

If that doesn't work:
```cmd
python -m pip install requests beautifulsoup4 pandas tqdm
```

---

### ❌ Permission Denied When Saving CSV

**Error**: `PermissionError: [Errno 13] Permission denied`

**Solutions**:

1. **Close the CSV file** if it's open in Excel
2. **Run as Administrator**:
   - Right-click Command Prompt → "Run as administrator"
   - Navigate to folder and run script again
3. **Change output folder** in `config.json`:
   ```json
   {
     "save_to_downloads": false,
     "output_folder": "my_job_results"
   }
   ```

---

### ❌ Script Window Closes Immediately

**Problem**: Double-clicked the .py file but window closes before you can see anything

**Solution**: Don't double-click the .py file! Instead:
1. Open Command Prompt
2. Navigate to the folder
3. Run `python linkedin_job_scraper.py`

Or use the `.bat` shortcut from Step 5 (it includes `pause` to keep the window open).

---

# 🍎 SECTION 2: Mac Setup (macOS Monterey, Ventura, Sonoma)

## Step 1: Install Python

Good news! Macs often come with Python pre-installed. Let's check!

### 1.1 Check If Python Is Installed

1. Open **Terminal**:
   - Press `Cmd + Space` to open Spotlight
   - Type `Terminal` and press Enter

2. Type this command and press Enter:

   ```bash
   python3 --version
   ```

3. **If you see** `Python 3.x.x`:
   
   ```
   Python 3.11.4
   ```
   
   ✅ **Great!** Python is already installed. Skip to [Step 2](#step-2-download-the-script-1).

4. **If you see** `command not found`:
   
   Continue below to install Python.

### 1.2 Install Python (Method A: Download from python.org)

1. Go to: **[python.org/downloads/macos](https://www.python.org/downloads/macos/)**
2. Click **"Download Python 3.11.x"**
3. Open the downloaded `.pkg` file
4. Follow the installer (click Continue → Continue → Agree → Install)
5. Enter your Mac password when prompted
6. Click **Close** when done

### 1.3 Install Python (Method B: Using Homebrew - Recommended)

Homebrew is a package manager that makes installing software easier on Mac.

**Install Homebrew first** (skip if you already have it):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This command will ask for your password—that's normal!

**Then install Python**:

```bash
brew install python
```

### 1.4 Verify Installation

```bash
python3 --version
```

You should see:
```
Python 3.11.x
```

✅ **Success!** Python is ready.

---

## Step 2: Download the Script

### 2.1 Download ZIP from GitHub

1. Go to the GitHub repository page
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. The ZIP file will download to your **Downloads** folder

### 2.2 Extract the Files

1. Open **Finder**
2. Go to **Downloads**
3. Double-click the ZIP file to extract it
4. Drag the extracted folder to your preferred location:
   - **Recommended**: `Documents` folder
   - Or: `Desktop`

### 2.3 Note the Folder Path

Remember where you put the folder. For example:
- `/Users/yourname/Documents/linkedin-job-scraper`
- `/Users/yourname/Desktop/linkedin-job-scraper`

> 💡 **Tip**: In Finder, you can drag the folder into Terminal to auto-fill its path!

---

## Step 3: Install Required Libraries

### 3.1 Open Terminal

- Press `Cmd + Space`
- Type `Terminal`
- Press Enter

### 3.2 Navigate to the Script Folder

If you put the folder in Documents:

```bash
cd ~/Documents/linkedin-job-scraper
```

If you put it on Desktop:

```bash
cd ~/Desktop/linkedin-job-scraper
```

> 💡 **What does `~` mean?** It's a shortcut for your home folder (`/Users/yourname`).

### 3.3 Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3.4 What Success Looks Like

```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.12.2-py3-none-any.whl (142 kB)
Successfully installed beautifulsoup4-4.12.2 pandas-2.0.3 requests-2.31.0 tqdm-4.66.1
```

✅ **All libraries installed!**

### 3.5 If You Get a Permission Error

If you see `Permission denied` or `externally-managed-environment`:

**Option 1**: Add `--user` flag:
```bash
pip3 install -r requirements.txt --user
```

**Option 2**: Use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Option 3** (if using Homebrew Python):
```bash
pip3 install -r requirements.txt --break-system-packages
```

---

## Step 4: Run the Script

### 4.1 Start the Script

In Terminal (still in the script folder), type:

```bash
python3 linkedin_job_scraper.py
```

### 4.2 Follow the Prompts

```
============================================================
         🔗 LinkedIn Job Scraper v2.0
============================================================

📁 Output folder: /Users/yourname/Downloads/job_results
⚙️  Edit config.json to change default settings.

📋 Enter job title (e.g., 'Python Developer'): Product Manager
📍 Enter location (default: India): San Francisco
🔢 How many jobs? (default: 50, max: 500): 100
```

### 4.3 Find Your CSV File

The CSV file is saved to:
```
~/Downloads/job_results/linkedin_jobs_Product_Manager_San_Francisco_20260203_143052.csv
```

To open it:
1. Open **Finder**
2. Go to **Downloads** → **job_results**
3. Double-click the CSV file (opens in Numbers or Excel)

Or open with Google Sheets:
1. Go to [sheets.google.com](https://sheets.google.com)
2. File → Import → Upload → Select your CSV

---

## Step 5: Optional - Create Alias for Easy Running

Instead of typing the full command every time, let's create a shortcut!

### 5.1 Determine Your Shell

Most modern Macs use `zsh`. Check with:

```bash
echo $SHELL
```

If it says `/bin/zsh`, you use zsh. If `/bin/bash`, you use bash.

### 5.2 Edit Your Shell Profile

For **zsh** (most Macs):
```bash
nano ~/.zshrc
```

For **bash** (older Macs):
```bash
nano ~/.bash_profile
```

### 5.3 Add the Alias

In the nano editor, add this line at the bottom (adjust path if needed):

```bash
alias jobscraper='cd ~/Documents/linkedin-job-scraper && python3 linkedin_job_scraper.py'
```

### 5.4 Save and Exit

1. Press `Ctrl + O` (letter O, not zero)
2. Press `Enter` to confirm
3. Press `Ctrl + X` to exit

### 5.5 Reload Your Profile

```bash
source ~/.zshrc
```

(Or `source ~/.bash_profile` for bash)

### 5.6 Use Your Shortcut!

Now, from anywhere in Terminal, just type:

```bash
jobscraper
```

And the scraper will start! 🎉

---

## 🔧 Troubleshooting Mac

### ❌ SSL Certificate Error

**Error**: `ssl.SSLCertVerificationError: certificate verify failed`

This is common on macOS. **Solutions**:

**Solution 1**: Run the certificate installer:
```bash
# For Python 3.11 (adjust version number as needed)
/Applications/Python\ 3.11/Install\ Certificates.command
```

**Solution 2**: Install/upgrade certifi:
```bash
pip3 install --upgrade certifi
```

**Solution 3**: If using Homebrew Python:
```bash
brew reinstall openssl
```

---

### ❌ "pip3 not found"

**Solution**: Use Python's built-in pip:
```bash
python3 -m pip install -r requirements.txt
```

---

### ❌ Permission Issues

**Error**: `Permission denied` when running the script

**Solution**: Make the script executable:
```bash
chmod +x linkedin_job_scraper.py
```

Then run with:
```bash
./linkedin_job_scraper.py
```

---

### ❌ M1/M2/M3 Mac (Apple Silicon) Issues

Apple Silicon Macs might have compatibility notes:

1. **Make sure you have the right Python**:
   ```bash
   file $(which python3)
   ```
   Should say `arm64` or `Mach-O universal binary`

2. **If you get architecture errors**:
   ```bash
   arch -arm64 pip3 install -r requirements.txt
   ```

3. **Rosetta 2** (for Intel compatibility):
   Most people don't need this, but if dependencies fail:
   ```bash
   softwareupdate --install-rosetta
   ```

The scraper should work natively on Apple Silicon without issues!

---

# 🎯 SECTION 3: First Run Walkthrough

## What You'll See When Running

Here's a detailed breakdown of each step:

### 3.1 Welcome Screen

```
============================================================
🖥️  Platform: Darwin 23.0.0
🐍 Python: 3.11.4
============================================================

============================================================
         🔗 LinkedIn Job Scraper v2.0
============================================================

📁 Output folder: /Users/yourname/Downloads/job_results
⚙️  Edit config.json to change default settings.
```

This confirms the script is running correctly and shows where files will be saved.

### 3.2 Job Title Prompt

```
📋 Enter job title (e.g., 'Python Developer'): 
```

**What to enter**: The job title you're looking for.

**Examples**:
- `Product Manager`
- `Software Engineer`
- `Data Analyst`
- `Marketing Manager`
- `UX Designer`

> 💡 **Tip**: Be specific! "Senior Software Engineer" will give different results than "Software Engineer"

### 3.3 Location Prompt

```
📍 Enter location (default: India): 
```

**What to enter**: Where you want to work.

**Examples**:
- `San Francisco, CA`
- `New York`
- `Remote`
- `London, UK`
- `Singapore`

> 💡 **Tip**: Use "Remote" to find work-from-home jobs!

### 3.4 Number of Jobs

```
🔢 How many jobs? (default: 50, max: 500): 
```

**What to enter**: How many job listings to scrape.

**Recommendations**:
- **First run**: Start with `25-50` to make sure everything works
- **Regular use**: `100-200` is a good balance
- **Maximum**: `500` (takes longer)

### 3.5 Experience Level

```
📊 Experience level options:
   1. Internship
   2. Entry level
   3. Associate
   4. Mid-Senior level
   5. Director
   6. Executive
   7. All levels (no filter)

📊 Select experience level (1-7, default: 7): 
```

**What to enter**: A number 1-7, or press Enter for all levels.

### 3.6 JSON Export

```
💾 Also export as JSON? (y/n, default: n): 
```

**What to enter**: 
- `n` or just press Enter (most people don't need JSON)
- `y` if you want data in JSON format too (for programmers)

### 3.7 Confirmation

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Job Title:       Product Manager
📍 Location:        San Francisco
🔢 Jobs to scrape:  100
📊 Experience:      All levels
⏱️  Estimated time:  ~10 seconds
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Start scraping? (y/n): 
```

**What to enter**: `y` to start, or `n` to go back and change settings.

### 3.8 Progress Bar

```
🌐 Checking internet connection...
✅ Internet connection OK

Scraping jobs: |████████████████████| 100/100 (100%) [0:00:45<0:00:00]
```

Just wait while the magic happens! ✨

### 3.9 Completion

```
✅ Successfully scraped 97 jobs
✅ Removed 3 duplicate listings
✅ CSV saved to: /Users/yourname/Downloads/job_results/linkedin_jobs_Product_Manager_San_Francisco_20260203_143052.csv
✅ Execution time: 0 min 45 sec
```

🎉 **Done!** Your job listings are ready!

---

## Understanding the Output CSV

Open your CSV file in Excel, Numbers, or Google Sheets. Here's what each column means:

| Column | Description | Example |
|--------|-------------|---------|
| **Job Title** | The position name | Senior Product Manager |
| **Company** | Who's hiring | Google |
| **Location** | Where the job is | Mountain View, CA |
| **URL** | Link to full listing | https://linkedin.com/jobs/view/... |
| **Posted Date** | When it was posted | 2 days ago |

### Opening in Excel

1. Double-click the CSV file
2. If it opens with weird formatting, try:
   - File → Open
   - Select the CSV file
   - Choose "Delimited" → "Comma" as separator
   - Set encoding to "UTF-8"

### Opening in Google Sheets

1. Go to [sheets.google.com](https://sheets.google.com)
2. Click **Blank** to create new spreadsheet
3. File → Import → Upload
4. Drag your CSV file or click to browse
5. Import location: "Replace spreadsheet"
6. Separator type: "Comma"
7. Click **Import data**

### What If Some Fields Say "N/A"?

This is normal! It means LinkedIn didn't provide that information for the job listing. Common reasons:
- The company hid the posting date
- Location wasn't specified
- The listing has limited details

---

# ⚙️ SECTION 4: Customization

## Editing config.json

You can customize how the scraper behaves by editing `config.json`.

### Finding the File

The `config.json` file is in the same folder as the main script:

```
📁 linkedin-job-scraper
 ├── 📄 linkedin_job_scraper.py
 ├── 📄 config.json  ← Edit this file
 ├── 📄 requirements.txt
 └── 📄 README.md
```

### Opening for Editing

**Windows**:
- Right-click `config.json` → Open with → Notepad

**Mac**:
- Right-click `config.json` → Open With → TextEdit
- Or in Terminal: `nano config.json`

### Default Settings Explained

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

| Setting | What It Does | Recommended Value |
|---------|--------------|-------------------|
| `default_location` | Pre-filled location when you press Enter | Your city or "Remote" |
| `default_num_jobs` | Pre-filled number of jobs | 50-100 |
| `max_jobs_limit` | Maximum jobs allowed per run | 500 |
| `output_folder` | Name of output folder | "job_results" |
| `delay_between_requests` | Seconds between requests (prevents blocking) | 2.5-5 |
| `max_retries` | How many times to retry failed requests | 3 |
| `timeout_seconds` | How long to wait for a response | 30 |
| `save_to_downloads` | Save to Downloads folder (true) or script folder (false) | true |
| `export_json` | Also save as JSON by default | false |
| `show_progress_bar` | Show the progress bar | true |
| `log_to_file` | Save detailed logs | true |

### Example: Customize for Your Job Search

If you're in San Francisco looking for remote jobs:

```json
{
    "default_location": "Remote",
    "default_num_jobs": 100,
    "delay_between_requests": 3,
    "save_to_downloads": true
}
```

> ⚠️ **Important**: Save the file and restart the script for changes to take effect!

---

## Scheduling Automatic Runs

Want the scraper to run automatically every week? Here's how!

### Windows: Task Scheduler

1. Press `Windows Key`, type `Task Scheduler`, press Enter

2. Click **Create Basic Task...**

3. **Name**: "LinkedIn Job Scraper"
   **Description**: "Automatically scrape jobs weekly"

4. **Trigger**: Select "Weekly"
   - Choose your preferred day (e.g., Monday)
   - Set time (e.g., 9:00 AM)

5. **Action**: Select "Start a program"

6. **Program/script**: Browse to your `.bat` file
   - Example: `C:\Users\YourName\Desktop\Run Job Scraper.bat`

7. **Finish**: Check "Open Properties dialog" and click Finish

8. In Properties, under **Conditions**, uncheck "Start only if computer is on AC power" (if you want it to run on battery too)

9. Click **OK**

Now the scraper will run automatically every Monday at 9 AM!

### Mac: Using Cron Jobs

1. Open Terminal

2. Edit your crontab:
   ```bash
   crontab -e
   ```

3. If asked to choose an editor, type `1` for nano

4. Add this line (runs every Monday at 9 AM):
   ```
   0 9 * * 1 cd ~/Documents/linkedin-job-scraper && /usr/bin/python3 linkedin_job_scraper.py --auto
   ```

   > 📝 **Cron format**: `minute hour day month weekday command`

5. Save and exit (`Ctrl+O`, Enter, `Ctrl+X`)

6. Verify:
   ```bash
   crontab -l
   ```

### Mac: Using Automator (Easier GUI Method)

1. Open **Automator** (Cmd+Space, type "Automator")

2. Choose **Calendar Alarm**

3. Search for "Run Shell Script" and drag it to the workflow

4. Enter:
   ```bash
   cd ~/Documents/linkedin-job-scraper
   /usr/bin/python3 linkedin_job_scraper.py
   ```

5. File → Save as "LinkedIn Job Scraper"

6. A calendar event is created. Double-click it to set:
   - Repeat: Weekly
   - Day: Monday
   - Time: 9:00 AM

---

# ❓ SECTION 5: FAQ

### Q: Do I need to keep the Terminal/Command Prompt window open?

**A**: Yes, while the script is running. You'll see live progress updates. Once it says "✅ Successfully scraped X jobs", you can close it.

---

### Q: How long does it take to scrape 100 jobs?

**A**: Typically **1-3 minutes** depending on:
- Your internet speed
- The delay setting (default is 2.5 seconds between requests)
- LinkedIn's server response time

For 100 jobs with default settings: expect ~2 minutes.

---

### Q: Can I run multiple searches at once?

**A**: **No**, please don't. Running multiple instances simultaneously will:
- Get you rate-limited faster
- Potentially get your IP blocked
- Mix up your results

Run searches **one after another**. If you need multiple searches, wait for one to finish before starting the next.

---

### Q: The CSV has weird characters (encoding issues)

**A**: This happens when the file isn't opened with UTF-8 encoding.

**Fix for Excel**:
1. Open Excel
2. File → Import (not Open!)
3. Select "CSV file"
4. Choose your file
5. In the wizard, set **File origin** to "65001: Unicode (UTF-8)"
6. Click Finish

**Fix for Google Sheets**:
- Just upload directly; Google Sheets handles UTF-8 automatically

---

### Q: LinkedIn blocked me, what now?

**A**: If you see "403 Forbidden" or "429 Too Many Requests":

1. **Wait 30-60 minutes** before trying again
2. **Reduce the number of jobs** in your next run (try 25-50)
3. **Increase the delay** in config.json:
   ```json
   {
       "delay_between_requests": 5
   }
   ```
4. **Try a VPN** (changes your IP address)
5. **Don't scrape too often** - once or twice a day is plenty

---

### Q: Can I search for remote jobs only?

**A**: Yes! Two ways:

**Method 1**: Use "Remote" as your location:
```
📍 Enter location: Remote
```

**Method 2**: Include "remote" in the job title:
```
📋 Enter job title: Remote Product Manager
```

---

### Q: Why did I get fewer jobs than requested?

**A**: Several possible reasons:

1. **Not enough listings**: LinkedIn might not have 500 "Quantum Physics Professor" jobs in "Smalltown, Iowa"
2. **Duplicates removed**: The script automatically removes duplicate listings
3. **Invalid listings**: Some job cards might be malformed and get skipped

The number you enter is the **maximum**—actual results depend on availability.

---

### Q: Is this legal? Will I get in trouble?

**A**: This script scrapes **publicly available** job listings (the same ones you'd see without logging in). However:

- ✅ For personal use (job searching) = Generally okay
- ⚠️ Respect LinkedIn's servers (don't scrape thousands of jobs daily)
- ⚠️ Don't sell or redistribute the data commercially
- ❌ Don't use this to spam companies or recruiters

When in doubt, use responsibly and don't overdo it!

---

### Q: Can I scrape jobs from other countries?

**A**: Absolutely! Just enter the country or city in the location field:

- `Germany`
- `Berlin, Germany`
- `United Kingdom`
- `London, UK`
- `Australia`
- `Sydney, NSW`

---

### Q: How do I update the script?

**A**: If you downloaded from GitHub:

1. Download the latest ZIP
2. Extract and replace the old files
3. Your `config.json` settings will be preserved if you don't overwrite it

---

# 🆘 SECTION 6: Getting Help

## If You Encounter Issues

### Step 1: Check the Troubleshooting Sections

Scroll up to the troubleshooting section for your platform:
- [Windows Troubleshooting](#-troubleshooting-windows)
- [Mac Troubleshooting](#-troubleshooting-mac)

### Step 2: Check the Log File

Every run creates a log file with detailed information:

**Location**: Same folder as your CSV output
```
📁 job_results
 ├── 📄 linkedin_jobs_Product_Manager_...csv
 └── 📄 scraper_log_20260203_143052.txt  ← Check this!
```

Open the log file to see:
- Exact error messages
- Which step failed
- Technical details

### Step 3: Common Error Solutions Quick Reference

| Error Message | Quick Fix |
|--------------|-----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `SSLCertVerificationError` | Run `pip install --upgrade certifi` |
| `ConnectionError` | Check your internet connection |
| `403 Forbidden` | Wait 30+ minutes, then try with fewer jobs |
| `429 Too Many Requests` | Wait 1 hour, increase delay in config.json |
| `PermissionError` | Close the CSV if open, or run as admin |
| `FileNotFoundError` | Make sure you're in the correct folder |

### Step 4: Contact for Support

If you're still stuck, reach out with:

1. **Your operating system** (Windows 10, macOS Sonoma, etc.)
2. **Python version** (`python --version` or `python3 --version`)
3. **The exact error message** (copy-paste from Terminal/Command Prompt)
4. **What you were trying to do** when it failed

📧 **Email**: [Your email here]

🐛 **GitHub Issues**: [Link to your GitHub issues page]

---

# 🎬 SECTION 7: Video Tutorial

> 📺 **Coming Soon!**

Watch the step-by-step setup walkthrough for your platform:

### Windows Tutorial
🎥 **[YouTube Link - Windows Setup]** *(Coming Soon)*
- Installing Python
- Downloading the script
- Running your first scrape
- Creating a desktop shortcut

### Mac Tutorial  
🎥 **[YouTube Link - Mac Setup]** *(Coming Soon)*
- Checking for Python
- Installing via Homebrew
- Terminal basics
- Creating an alias

### Quick Start (Both Platforms)
🎥 **[YouTube Link - Quick Start]** *(Coming Soon)*
- 3-minute speed run
- From zero to scraped jobs

---

## 🎉 You're All Set!

Congratulations on setting up the LinkedIn Job Scraper! 

Here's a quick recap of what you can do now:

| Action | Command |
|--------|---------|
| Run the scraper | `python linkedin_job_scraper.py` (Windows) or `python3 linkedin_job_scraper.py` (Mac) |
| Find your results | Check `Downloads/job_results/` |
| Customize settings | Edit `config.json` |
| Run easily | Use your `.bat` shortcut (Windows) or alias (Mac) |

---

## 💡 Pro Tips for Job Searching

1. **Run weekly**: Set up automatic scheduling to get fresh listings
2. **Use specific titles**: "Senior Product Manager" vs just "Product Manager"
3. **Try variations**: "PM", "Product Manager", "Product Lead"
4. **Export to Google Sheets**: Easier to filter, sort, and track applications
5. **Add columns**: Track which jobs you applied to, interview status, etc.

---

<div align="center">

**Happy job hunting! 🚀**

*Made with ❤️ to help job seekers everywhere*

---

*Last updated: February 2026*

</div>
