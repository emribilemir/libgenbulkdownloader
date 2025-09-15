# Libgen Bulk Downloader

This script downloads e-books in EPUB format from Library Genesis in bulk, based on a list of ISBNs.

## Requirements

*   Python 3
*   [aria2](https://aria2.github.io/): A command-line download utility.

## Installation

1. **Install Aria2:**
    * It is recommended to install via the [Chocolatey](https://chocolatey.org/) package manager on Windows:
        ```bash
        choco install aria2
        ```
    * To easily install Chocolatey, open PowerShell **as Administrator** and run the following command:
        ```powershell
        Set-ExecutionPolicy Bypass -Scope Process -Force; 
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; 
        iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        ```

2.  **Clone the repository and install Python dependencies:**
    ```bash
    git clone <repository-url>
    cd libgenbulkdownloader
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal:
```bash
python main.py
```
The script will prompt you to choose one of two options:

1.  **Paste ISBNs directly:** You can copy your list of ISBNs and paste them into the terminal.
2.  **Use `isbn.txt`:** The script can read the ISBNs from the `isbn.txt` file. If you choose this option, make sure you have added the ISBNs of the books you want to download to this file, with each ISBN on a new line.

The script will then find the EPUB versions of the books and download them into the project directory.

## Credits
This project utilizes the `libgen-api-enhanced` library.

*   **GitHub Repository:** [https://github.com/onurhanak/libgen-api-enhanced](https://github.com/onurhanak/libgen-api-enhanced)
