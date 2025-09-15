# Libgen Bulk Downloader

This script downloads e-books in EPUB format from Library Genesis in bulk, based on a list of ISBNs.

## Requirements

*   Python 3
*   [aria2](https://aria2.github.io/): A command-line download utility.

## Installation

1.  **Install aria2:**
    *   It is recommended to install via the [Chocolatey](https://chocolatey.org/) package manager on Windows:
        ```bash
        choco install aria2
        ```

2.  **Clone the repository and install Python dependencies:**
    ```bash
    git clone <repository-url>
    cd libgenbulkdownloader
    pip install -r requirements.txt
    ```

## Usage

1.  Open the `isbn.txt` file and add the ISBNs of the books you want to download. Each ISBN should be on a new line.
2.  Run the script from your terminal:
    ```bash
    python main.py
    ```
3.  The script will find the EPUB versions of the books and download them into the project directory.

## Credits
This project utilizes the `libgen-api-enhanced` library.

*   **GitHub Repository:** [https://github.com/onurhanak/libgen-api-enhanced](https://github.com/onurhanak/libgen-api-enhanced)