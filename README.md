# Automated Process Logger & Scheduling System

## 📌 Project Description

The **Automated Process Logger & Scheduling System** is a Python-based automation project that monitors running processes and records their details in timestamped log files at scheduled intervals.

The system collects process information such as Process ID (PID), process name, username, process status, and memory usage. It uses the `psutil` library to retrieve process details and the `schedule` library to automate periodic logging.

This project helps automate process monitoring, maintain system activity records, and generate organized log reports.

## 🚀 Features

* **Process Monitoring:** Retrieves information about currently running processes.
* **Process ID Tracking:** Records the unique PID of each process.
* **Process Information:** Collects process name, username, and status.
* **Memory Monitoring:** Records the memory usage percentage of each process.
* **Automated Logging:** Generates log files containing process information.
* **Timestamp-Based Filenames:** Creates uniquely named log files using the current date and time.
* **Task Scheduling:** Executes process logging automatically at a user-defined interval.
* **Command-Line Interface:** Supports help, usage, and execution commands.
* **Error Handling:** Handles inaccessible, terminated, and zombie processes.

## 🛠️ Technologies Used

* Python
* psutil
* schedule
* os
* sys
* time
* datetime

## 📂 Project Structure

```text
Automated_Process_Logger_Scheduling_System/
│
├── process_Looger.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── ProcessLogs/
    ├── ProcessLog_17_10_2026_10_00_00.log
    ├── ProcessLog_17_10_2026_10_01_00.log
    └── ...
```

*Note: The `ProcessLogs` directory and its log files are generated when the program runs. The filenames above are examples.*

## ⚙️ Installation

### Step 1: Install Python

Install Python on your system if it is not already installed.

Verify the installation:

```bash
python --version
```

### Step 2: Open the Project Directory

Open Command Prompt and navigate to your project directory.

Example:

```cmd
cd /d D:\Project_Github\AUTOMATION_PROJECT\Automated_Process_Logger_Scheduling_System
```

Replace the example path with your actual project directory.

### Step 3: Install Required Libraries

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure requirements.txt

Add the following libraries to `requirements.txt`:

```text
psutil
schedule
```

The `os`, `sys`, `time`, and `datetime` modules are included with Python and do not require separate installation.

## ▶️ How to Run the Project

### 1. Display Help

```bash
python process_Looger.py --h
```

Displays the project name, command syntax, and an execution example.

### 2. Display Usage Instructions

```bash
python process_Looger.py --u
```

Displays the required command-line arguments.

### 3. Start Automated Process Logging

```bash
python process_Looger.py 1 ProcessLogs
```

**Command arguments:**

* `1`: Specifies the logging interval in minutes.
* `ProcessLogs`: Specifies the directory where log files will be stored.

The scheduler generates the first log after the specified interval and continues logging at the configured interval.

Press `Ctrl + C` to stop the program.

## 📄 Sample Log Report

The generated log files contain information similar to the following:

```text
============================================================
 AUTOMATED PROCESS LOGGER REPORT
============================================================
Author Name : Yash Chavan
Date & Time : 2026-10-17 10:00:00
Total Processes : 3
============================================================

------------------------------------------------------------
PID            : 1234
Process Name   : python.exe
Username       : User
Process Status : running
Memory Usage   : 1.25%
------------------------------------------------------------

------------------------------------------------------------
PID            : 5678
Process Name   : explorer.exe
Username       : User
Process Status : running
Memory Usage   : 0.85%
------------------------------------------------------------

============================================================
```

*Note: The process details and values shown above are illustrative examples. Actual output depends on your computer and currently running processes.*

## 🎯 Applications

* Monitoring running system processes.
* Recording process information for later analysis.
* Automating periodic process logging.
* Tracking individual process memory usage.
* Practicing Python automation and system monitoring.
* Learning command-line argument handling and task scheduling.

## 🔮 Future Enhancements

* Add CPU utilization tracking for individual processes.
* Generate CSV and JSON reports.
* Add email notifications for important process events.
