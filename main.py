import datetime
from time import sleep
import scraper

job_dict = {}

# Want to change the day and time of the alert? Change the values below
day_of_alert = 'Fri'  # Just the first three letters of the day
hour_of_alert = 14  # hours in 24 hr format
min_of_alert = 53


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


def main():
    while True:
        if get_day() == day_of_alert and get_hour() == hour_of_alert and get_min() == min_of_alert and get_sec() == 10:
            job_dict['Ideo'] = scraper.ideo_scraper()
            job_dict['Frog'] = scraper.frog_scraper()
            job_dict['Ammunition'] = scraper.ammo_scraper()

            for x, y in job_dict.items():
                print(x, y)
            sleep(2)
        else:
            pass


if __name__ == '__main__':
    main()
