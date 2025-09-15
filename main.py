import subprocess
import re
from libgen_api_enhanced import LibgenSearch
import sys

def sanitize_filename(name):
    """Sanitizes the filename to be valid for Windows, replacing invalid characters with an underscore."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)[:100]  # Limit to 100 characters

def download_books(isbns):
    """Downloads books for the given list of ISBNs."""
    s = LibgenSearch()
    for isbn in isbns:
        if not isbn:  # Skip empty lines
            continue
        print(f"Searching for ISBN: {isbn}")
        results = s.search_default(isbn)
        found = False
        for book in results:
            if book.extension.lower() == "epub":
                try:
                    book.resolve_direct_download_link()
                    link = book.resolved_download_link
                    safe_title = sanitize_filename(book.title)
                    file_name = f"{safe_title}_{isbn}.epub"
                    print(f"Downloading: {file_name} -> {link}")

                    subprocess.run([
                        "aria2c",
                        "-x", "16",
                        "-s", "16",
                        "-d", ".",
                        "-o", file_name,
                        link
                    ], check=True)
                    found = True
                    break  # Move to the next ISBN after successful download
                except Exception as e:
                    print(f"Error downloading book with ISBN {isbn}: {e}")
        if not found:
            print(f"No EPUB found for ISBN: {isbn}")

def main():
    """Main function to run the script."""
    print("Choose an option:")
    print("1: To paste your ISBN lists to copy to the new_string.")
    print("2: If you want me to query the isbn.txt file.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("Paste your ISBNs, separated by new lines. Press Ctrl+Z (Windows) or Ctrl+D (Linux/macOS) when you are finished.")
        isbns = [line.strip() for line in sys.stdin.readlines()]
        download_books(isbns)
    elif choice == '2':
        try:
            with open("isbn.txt", "r") as f:
                isbns = [line.strip() for line in f.readlines() if line.strip()]
            if not isbns:
                print("isbn.txt is empty. Please add ISBNs to the file.")
                return
            print(f"Found {len(isbns)} ISBNs in isbn.txt.")
            download_books(isbns)
        except FileNotFoundError:
            print("Error: isbn.txt not found. Please create it in the same directory as the script.")
    else:
        print("Invalid choice. Please run the script again and choose 1 or 2.")

if __name__ == "__main__":
    main()