# ============================================================
# Project Name : Automated Process Logger & Scheduling System
# Author Name  : Yash Chavan
# Date         : 01/10/2026
# Description  : Automatically monitors running processes and
#                records process details in timestamped log files
#                at scheduled intervals.
# ============================================================

import psutil
import sys
import os
import time
import schedule
from datetime import datetime


# ============================================================
# Step 1 : ProcessScan()
# Purpose : Collect details of currently running processes
# ============================================================

def ProcessScan():

    ProcessList = []

    # Scan all running processes
    for Process in psutil.process_iter(
        ['pid', 'name', 'username', 'status', 'memory_percent']
    ):

        try:

            ProcessInfo = Process.info

            # Store process information
            ProcessList.append({
                'PID': ProcessInfo['pid'],
                'Name': ProcessInfo['name'],
                'Username': ProcessInfo['username'],
                'Status': ProcessInfo['status'],
                'Memory': ProcessInfo['memory_percent']
            })

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            # Skip processes that cannot be accessed
            continue

    return ProcessList


# ============================================================
# Step 2 : ProcessLogger()
# Purpose : Generate a timestamped process log file
# ============================================================

def ProcessLogger(FolderName):

    # Create the folder if it does not exist
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)

    # Generate current date and time
    CurrentTime = datetime.now()

    # Create a unique log filename
    FileName = CurrentTime.strftime(
        "ProcessLog_%d_%m_%Y_%H_%M_%S.log"
    )

    FilePath = os.path.join(FolderName, FileName)

    # Scan running processes
    ProcessList = ProcessScan()

    # Write process details into the log file
    with open(FilePath, "w", encoding="utf-8") as LogFile:

        LogFile.write("=" * 60 + "\n")
        LogFile.write(" AUTOMATED PROCESS LOGGER REPORT\n")
        LogFile.write("=" * 60 + "\n")

        LogFile.write(
            f"Author Name : Yash Chavan\n"
        )

        LogFile.write(
            f"Date & Time : {CurrentTime}\n"
        )

        LogFile.write(
            f"Total Processes : {len(ProcessList)}\n"
        )

        LogFile.write("=" * 60 + "\n\n")

        # Record each process
        for Process in ProcessList:

            LogFile.write("-" * 60 + "\n")

            LogFile.write(
                f"PID            : {Process['PID']}\n"
            )

            LogFile.write(
                f"Process Name   : {Process['Name']}\n"
            )

            LogFile.write(
                f"Username       : {Process['Username']}\n"
            )

            LogFile.write(
                f"Process Status : {Process['Status']}\n"
            )

            LogFile.write(
                f"Memory Usage   : {Process['Memory']:.2f}%\n"
            )

            LogFile.write("-" * 60 + "\n\n")

    print(f"[SUCCESS] Process log created: {FilePath}")


# ============================================================
# Step 3 : main()
# Purpose : Handle command-line arguments and scheduling
# ============================================================

def main():

    # Display help information
    if len(sys.argv) == 2 and sys.argv[1] == "--h":
        print("Automated Process Logger & Scheduling System")
        print("Usage: python ProcessLogger.py <Minutes> <FolderName>")
        print("Example: python ProcessLogger.py 1 ProcessLogs")
        return

    # Display usage information
    if len(sys.argv) == 2 and sys.argv[1] == "--u":
        print("Usage: python ProcessLogger.py <Minutes> <FolderName>")
        return

    # Validate command-line arguments
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        print("Usage: python ProcessLogger.py <Minutes> <FolderName>")
        return

    try:
        Interval = int(sys.argv[1])

        if Interval <= 0:
            print("Interval must be greater than zero.")
            return

    except ValueError:
        print("Please enter the interval as a positive integer.")
        return

    FolderName = sys.argv[2]

    # Schedule process logging
    schedule.every(Interval).minutes.do(
        ProcessLogger, FolderName
    )

    print("=" * 60)
    print(" AUTOMATED PROCESS LOGGER & SCHEDULING SYSTEM")
    print("=" * 60)
    print(f"Author Name : Yash Chavan")
    print(f"Interval    : Every {Interval} minute(s)")
    print(f"Log Folder  : {FolderName}")
    print("Press Ctrl+C to stop the program.")
    print("=" * 60)

    try:
        # Run scheduled tasks continuously
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProcess Logger stopped successfully.")


# ============================================================
# Step 4 : Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()

# ============================================================
# End of Project
# ============================================================