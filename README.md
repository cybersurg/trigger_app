# Simple Trigger-Based Application

This is a basic Python application that demonstrates the core concepts of trigger-based automation.

## How it works
- **The Trigger:** Watches an `inbox` folder for new files.
- **The Condition:** Checks if the filename contains the word "urgent".
- **The Action:** Simulates sending a notification and moves the file to a `processed` folder.

## How to run
1. Ensure you have Python installed.
2. Run the script: `python trigger_app.py`
3. Drop a file named `urgent_report.txt` into the `inbox` folder to see the trigger fire!
