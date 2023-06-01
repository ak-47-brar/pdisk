import re
import requests

# Read URLs from upload.txt
with open('uploads.txt', 'r') as file:
    urls = file.readlines()

# Process each URL
updated_urls = []
for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace and newlines

    # Send a GET request to fetch the HTML content
    response = requests.get(url)
    html = response.text

    # Regular expression pattern to extract file size
    pattern = r'File Size: ([\d.]+) [A-Za-z]+'
    match = re.search(pattern, html)

    if match:
        file_size = match.group(1)
        updated_urls.append(f"{url.strip()} - File Size: {file_size}")
    else:
        updated_urls.append(f"{url.strip()} - File Size not found")

# Update upload.txt with URLs and file sizes
with open('uploads.txt', 'w') as file:
    file.write('\n'.join(updated_urls))

print("File sizes extracted and upload.txt updated.")
