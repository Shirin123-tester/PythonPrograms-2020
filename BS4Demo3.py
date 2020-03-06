from bs4 import BeautifulSoup # pip install beautifulsoup4
import requests # pip install requests
import sys
import re


url = "http://www.codekul.com/" 
response = None

try:
    response = requests.get(url)
except Exception as e:
    print(repr(e))
    sys.exit(1)

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')


for link in soup.find_all('a',attrs={'href':re.compile("^http://")}):
    print (link.get('href'))

