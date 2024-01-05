# Functionalities

- ***Event Viewer Log Collection:***
        Copies the Windows event log files, including Application.evtx, Security.evtx, and System.evtx, located in ***C:\Windows\System32\winevt\Logs\***, to the evidence directory.

- ***System Configuration File Collection:***
        Copies the system configuration files, such as sam, security, and system, ***located in C:\Windows\System32\config\, to the evidence directory.***

- ***Application Data Collection:***
        Retrieves application-relevant data files, including databases (.db), text files (.txt), and log files (.log), from specific directories in ***C:\Users\*\\AppData\Roaming and C :\Program Files\*\\AppData\Roaming.***

- ***Unique Evidence Directory Identification:***
        The evidence directory is named according to the machine name and a timestamp, ensuring uniqueness and facilitating organization.

- ***Completion Message Display:***
        After collection is complete, it displays a message indicating the directory where the evidence was stored.


The script is run from the command line and requires two mandatory arguments:

    machine_name: Name of the target machine.
    
    evidence_dir: Destination directory to store collected evidence

Example of use:

`python script.py machine_name C:\path\to\store\evidence`

# Dependencies

The script uses the following standard Python libraries:

           os
        shutil
         time
         argparse
         logging
         hashlib
         zipfile
         cryptography.fernet

# Possible Errors and Solutions

  ***Missing Arguments:***
        If the machine_name or evidence_dir arguments are missing, the script displays error messages. Be sure to provide both arguments.

   ***Insufficient Permissions:***
        Make sure that the user running the script has the necessary permissions to access the specified files and directories.

  ***Non-existent Destination Directory:***
        If the specified destination directory does not exist, the script will attempt to create it. However, make sure you have sufficient permissions to create directories in the specified path.

  ***Non-Existing Files:***
        If some of the specific files do not exist on the system, the script may fail when trying to copy them. Make sure these files are present on the target system.

- Be sure to review the evidence collected to ensure all relevant information is preserved.
