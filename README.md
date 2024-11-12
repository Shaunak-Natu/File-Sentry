# FileSentry

FileSentry is a simple script designed to monitor the presence of a specific file on the desktop (`iamhere.txt`). If the file is not found, the script automatically triggers an immediate system shutdown. This project is useful for creating a basic security layer, ensuring that the system stays operational only when a specified file is present.

## Features

- **File-Based Monitoring**: Monitors the desktop for a specific file (`iamhere.txt`).
- **Automated Shutdown**: Shuts down the system immediately if the file is missing.
- **Customizable Timing**: Allows for a delay before performing the check (default is 7 seconds).

## Requirements

- Python 3.x
- Windows OS (as the shutdown command in the script is tailored to Windows)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/SafeGuard.git
    cd SafeGuard
    ```

2. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. Convert the script into a standalone executable using PyInstaller.
1. Place the .exe file in the StartUp folder (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp). This will make the script runs automatically when the PC is turned on.
2. Create a file named `iamhere.txt` on your desktop. The script will check for this file’s presence.
3. The script will wait n seconds before checking for the presence of the file, i.e., you have n seconds to create the text file else the system will shut down.

## Customization

- **Change File Name**: To use a different file name, modify the script’s main function to check for a different file.
- **Adjust Shutdown Delay**: You can adjust the delay by changing the value of n. 

