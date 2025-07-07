import requests
from bs4 import BeautifulSoup
url = input("Enter or Paster the Url of the File: ").strip()
r = requests.get(str(url))
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())