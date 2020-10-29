import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep

job_dict = {}

# Want to change the day and time of the alert? Change the values below
day_of_alert = 'Thu'  # Just the first three letters of the day
hour_of_alert = 16  # hours in 24 hr format
min_of_alert = 57


def ideo_scraper():
    ideo_dict = {}
    ideo_url = 'https://www.ideo.com/jobs'
    ideo_page = requests.get(ideo_url)
    soup = BeautifulSoup(ideo_page.content, 'html.parser')
    elements = soup.findAll('li', class_='JobsListing--Item')

    for items in elements:
        details = []
        title_elem = items.find('span', class_='JobsListing--JobTitle')
        location_elem = items.find('p', class_='JobsListing--Location')
        url_elem = items.find('a', href=True)
        details.append(title_elem.text)
        details.append(location_elem.text)
        details.append('https://www.ideo.com' + url_elem['href'])
        ideo_dict[title_elem.text] = details
    return ideo_dict


def frog_scraper():
    frog_dict = {}
    frog_url = 'https://www.frogdesign.com/careers'
    frog_page = requests.get(frog_url)
    soup = BeautifulSoup(frog_page.content, 'html.parser')
    elements = soup.findAll('div', class_='StudioPositions_position__265h2')

    for items in elements:
        details = []
        title_elem = items.find('span', class_='StudioPositions_title__314h4')
        location_elem = items.find('span', class_='StudioPositions_studio__3TeSw')
        url_elem = items.find('a', href=True)
        details.append(title_elem.text)
        details.append(location_elem.text)
        details.append('https://www.frogdesign.com' + url_elem['href'])
        frog_dict[title_elem.text] = details

    return frog_dict


def get_day():
    current_time = datetime.datetime.now()
    return str(current_time.strftime("%a"))


def get_hour():
    current_time = datetime.datetime.now()
    return int(current_time.strftime("%H"))


def get_min():
    current_time = datetime.datetime.now()
    return int(current_time.strftime("%M"))


def get_sec():
    current_time = datetime.datetime.now()
    return int(current_time.strftime("%S"))


while True:
    # Want to change the date? Change
    if get_day() == day_of_alert and get_hour() == hour_of_alert and get_min() == min_of_alert and get_sec() == 10:
        job_dict['Ideo'] = ideo_scraper()
        job_dict['Frog'] = frog_scraper()

        for x, y in job_dict.items():
            print(x, y)
        sleep(2)
    else:
        pass
