import os
import shutil
import time
import argparse

def main():
  
    parser = argparse.ArgumentParser(description="Windows Machine Evidence Collection Script")
    parser.add_argument("machine_name", help="Machine name")
    parser.add_argument("evidence_dir", help="Evidence destination directory")
    args = parser.parse_args()

    machine_name = args.machine_name

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    evidence_dir = os.path.join(args.evidence_dir, f"{machine_name}_{timestamp}")
    os.makedirs(evidence_dir)
    
    log_files = [
        "C:\\Windows\\System32\\winevt\\Logs\\Application.evtx",
        "C:\\Windows\\System32\\winevt\\Logs\\Security.evtx",
        "C:\\Windows\\System32\\winevt\\Logs\\System.evtx",
    ]
    for log_file in log_files:
        shutil.copy2(log_file, evidence_dir)

    configuration_files = [
        "C:\\Windows\\System32\\config\\sam",
        "C:\\Windows\\System32\\config\\security",
        "C:\\Windows\\System32\\config\\system",
    ]
    for configuration_file in configuration_files:
        shutil.copy2(configuration_file, evidence_dir)
    
    app_data_dirs = [
        "C:\\Users\\*\\AppData\\Roaming",
        "C:\\Program Files\\*\\AppData\\Roaming",
    ]
    for app_data_dir in app_data_dirs:
        for root, dirs, files in os.walk(app_data_dir):
            for file in files:
                if file.endswith(".db") or file.endswith(".txt") or file.endswith(".log"):
                    shutil.copy2(os.path.join(root, file), evidence_dir)

    print(f"Evidence collected in {evidence_dir}.")

if __name__ == "__main__":
    main()
