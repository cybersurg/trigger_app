import os
import time
import shutil

# --- CONFIGURATION ---
INBOX_FOLDER = "inbox"
PROCESSED_FOLDER = "processed"

# Create folders if they don't exist
os.makedirs(INBOX_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Keep track of files we've already seen so we don't process them twice
processed_files = set()

print("🚀 Trigger App Started!")
print(f"👀 Watching folder: '{INBOX_FOLDER}'")
print("💡 Tip: Create a text file in the 'inbox' folder to test it.\n")

# --- THE MAIN EVENT LOOP ---
while True:
    try:
        # 1. THE TRIGGER: Detect new files in the inbox
        current_files = set(os.listdir(INBOX_FOLDER))
        new_files = current_files - processed_files

        for file in new_files:
            file_path = os.path.join(INBOX_FOLDER, file)
            
            # Ignore directories, only look at files
            if os.path.isfile(file_path):
                
                # 2. THE CONDITION: Check if it meets our rules
                if "urgent" in file.lower():
                    
                    # 3. THE ACTION: Execute the automated task
                    print(f"🚨 TRIGGER FIRED! Urgent file detected: {file}")
                    print("⏳ ACTION: Sending email notification to manager...")
                    
                    # Simulate network delay (sending an email)
                    time.sleep(1.5) 
                    
                    print(f"✅ SUCCESS: Notification sent for '{file}'!")
                    
                    # Move file to processed folder
                    shutil.move(file_path, os.path.join(PROCESSED_FOLDER, file))
                    print(f"📁 File moved to '{PROCESSED_FOLDER}'.\n")

                else:
                    # Action for non-matching conditions
                    print(f"ℹ️ File '{file}' does not meet conditions. Ignoring and archiving.")
                    shutil.move(file_path, os.path.join(PROCESSED_FOLDER, file))
                    print("-" * 40)

            # Mark file as processed so we don't trigger on it again
            processed_files.add(file)

        # Pause briefly before checking again (Polling interval)
        time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 App stopped by user.")
        break