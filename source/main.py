import requests
from bs4 import BeautifulSoup

url = "https://www.google.de"
#url = input("What url would you like to crawl for links? ")
if not url:
    print("No url was provided, exiting.")
    exit()

keyword = input("Name the key word within the link you are searching for (leave blank to list all links): ").strip()

all_links = []


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

# Output results
if all_links:
    for link in all_links:
        print(link)
else:
    print(f'The keyword "{keyword}" was not found.')