# Jiyufetch

## Overview

This project aims to provide a Python-based replacement for Neofetch, a command-line system information tool. It displays system information such as the operating system, release, version, machine architecture, CPU details, and more, along with customisable ASCII art.

### How it Works

The tool gathers system information using various methods depending on the operating system:

- **Linux**: It retrieves system information by reading system files such as `/etc/os-release`, `/etc/lsb-release`, `/etc/debian_version`, and `/etc/redhat-release`, or by executing commands like `lscpu`.
- **macOS**: It utilizes the `sysctl` command to fetch CPU details and platform-specific system information.
- **Windows**: It retrieves system information using the `wmic` command to get CPU details.

Once the system information is collected, the tool automatically detects the operating system and selects the appropriate ASCII art to display based on the detected system. The ASCII art for each operating system is defined in the `ascii_art.py` file.

### Features

- Display system information with customisable ASCII art.
- Automatically detects the operating system and displays relevant information.
- Support for Linux, macOS, and Windows platforms.

### Configuration

To configure the tool:
1. Install Python 
2. Clone this repository to your local machine.
3. Install the required dependencies using pip: `pip install -r requirements.txt` (coming soon).
4. Edit the `ascii_art.py` file to add ASCII art for specific operating systems if needed (won't be needed in the future).
5. Run the `Main.py` script: `python Main_1.py`.

### Work in Progress

Please note that this project is still a work in progress. Not all features have been implemented, and improvements are ongoing.

### To-Do

- Add ASCII art for additional operating systems (e.g., ArcoLinux, Arch, Ubuntu).
- Improve system detection and information retrieval.
- Enhance configuration options for customising output.
- Add support for additional system details.

### Contribution

Contributions are welcome! If you have any suggestions, bug fixes, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
