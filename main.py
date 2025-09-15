import subprocess
from libgen_api_enhanced import LibgenSearch
import re

# ISBN listesi
with open("isbn.txt", "r") as f:
    isbns = [line.strip() for line in f.readlines()]

s = LibgenSearch()


def sanitize_filename(name):
    # Windows için geçerli karakterleri bırak, diğerlerini _
    return re.sub(r'[<>:"/\\|?*]', '_', name)[:100]  # 100 karakterle sınırladık


for isbn in isbns:
    results = s.search_default(isbn)

    for book in results:
        if book.extension.lower() == "epub":
            book.resolve_direct_download_link()
            link = book.resolved_download_link
            safe_title = sanitize_filename(book.title)
            file_name = f"{safe_title}_{isbn}.epub"
            print(f"İndiriliyor: {file_name} -> {link}")

            subprocess.run([
                "aria2c",
                "-x", "16",
                "-s", "16",
                "-d", ".",
                "-o", file_name,
                link
            ])
            break
