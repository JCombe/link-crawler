import requests
from bs4 import BeautifulSoup
import re

url = "https://www.google.de"
#url = input("What url would you like to crawl for links? ")
if not url:
    print("No url was provided, exiting.")
    exit()

keyword = input("Name the key word within the link you are searching for (leave blank to list all links): ").strip()

all_links = []
all_absolute_paths = []


try:
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Raise HTTP errors (e.g. 404, 500)

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
    exit()

# Parse and search for links
content = response.content
soup = BeautifulSoup(content, 'html.parser')

a_tags = soup.find_all('a', href=True) # Filter tags with 'href' attribute

for a_tag in a_tags:
    href = a_tag['href']
    if not keyword or keyword.lower() in href.lower():
        all_links.append(href)

# Check if absolute path if not then make it an absolute path and append it to is_absolute_link array
def is_absolute_link(rel_path: str):
    pattern = re.compile(r'(https?)://')    # r: raw string literal; (): create a group e.g. (https?|ftp);
                                            # ^: caret, matches the beginning of a string
                                            # ?: the preceding character is optional
    if not pattern.match(rel_path):
        absolute_path = url+href
        all_absolute_paths.append(absolute_path)

    else:
        all_absolute_paths.append(rel_path)

# Calling is_absolute_link()
if all_links:
    for link in all_links:
        is_absolute_link(link)

# Recursively search for links


# Output results
if all_absolute_paths:
    for path in all_absolute_paths:
        print(path)
else:
    print(f'The keyword "{keyword}" was not found.')
