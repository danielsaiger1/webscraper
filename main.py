from bs4 import BeautifulSoup
import requests

url = 'https://www.stepstone.de/jobs/data-engineer'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
print(soup)