import requests
from bs4 import BeautifulSoup

job_dict = {}

# Get the open positions from IDEOs website and add them to our jobs dictionary
ideo_URL = 'https://www.ideo.com/jobs'
page = requests.get(ideo_URL)
soup = BeautifulSoup(page.content, 'html.parser')
elements = soup.findAll('li', class_='JobsListing--Item')

for items in elements:
    details = []
    title_elem = items.find('span', class_='JobsListing--JobTitle')
    location_elem = items.find('p', class_='JobsListing--Location')
    url_elem = items.find('a', href=True)
    string = 'company: Ideo, position: ' + title_elem.text + ', location: ' + location_elem.text
    details.append('Ideo')
    details.append(title_elem.text)
    details.append(location_elem.text)
    details.append('https://www.ideo.com' + url_elem['href'])
    job_dict[title_elem.text] = details

# Get the open positions from Frogs website and add them to our jobs dictionary
frog_URL = 'https://www.frogdesign.com/careers'
page = requests.get(frog_URL)
soup = BeautifulSoup(page.content, 'html.parser')
elements = soup.findAll('div', class_='StudioPositions_position__265h2')

for items in elements:
    details = []
    title_elem = items.find('span', class_='StudioPositions_title__314h4')
    location_elem = items.find('span', class_='StudioPositions_studio__3TeSw')
    url_elem = items.find('a', href=True)
    string = 'company: Frog, position: ' + title_elem.text + ', location: ' + location_elem.text
    details.append('Frog')
    details.append(title_elem.text)
    details.append(location_elem.text)
    details.append('https://www.frogdesign.com' + url_elem['href'])
    job_dict[title_elem.text] = details

for x, y in job_dict.items():
    print(x, y)
