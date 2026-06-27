# Automated Data Backup & Recovery Management System

## Project Overview

This project is a Python-based Backup and Recovery Management System. It allows users to create backups of files, maintain backup history, restore previous backups, generate logs, and store backup metadata.

## Features

* Create Manual Backups
* Backup Version Management
* View Backup History
* Restore Previous Backups
* Backup Logging
* Metadata Storage using JSON
* Command Line Interface (CLI)

## Technologies Used

* Python
* os
* shutil
* json
* datetime

## Project Structure

```
Task2/
│── main.py
│── Backup.log
│── metadata.json
│── SourceFiles/
│── Backups/
│── RestoreFolder/
└── README.md
```

## How to Run

1. Open the project in VS Code.
2. Run `main.py`.
3. Select an option from the menu:

   * Create Backup
   * View Backup History
   * Restore Backup
   * View Logs
   * Exit

## Features Implemented

* Manual Backup Creation
* Automatic Backup Version Naming using Timestamp
* Backup History
* Backup Restore
* Backup Logging
* Metadata Management
* Error Handling for Missing Source Folder

## Future Improvements

* Scheduled Backups
* Backup Compression
* Encryption
* Cloud Storage Integration
* Email Notifications

## Author

Developed by **Ehtisham Javaid**
