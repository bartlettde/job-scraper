import datetime
from time import sleep
import concurrent.futures
import threading
import sys

import scraper

job_dict = {}

# Want to change the day and time of the alert? Change the values below
day_of_alert = 'Mon'  # Just the first three letters of the day
hour_of_alert = 18  # hours in 24 hr format
min_of_alert = 43


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


def print_positions():
    job_dict['Ideo'] = scraper.ideo_scraper()
    job_dict['Frog'] = scraper.frog_scraper()
    job_dict['Ammunition'] = scraper.ammo_scraper()

    for x, y in job_dict.items():
        print(x, y)
    sleep(2)


def alarm_func():
    while True:
        if stop_threads:
            break
        if get_day() == day_of_alert and get_hour() == hour_of_alert and get_min() == min_of_alert and get_sec() == 10:
            if not scraper.ideo_scraper() or not scraper.frog_scraper() or not scraper.ammo_scraper():
                print('There is a connection issue and the update has not been sent. Reconnect your device to '
                      'the internet and the type "retry" into the console.')
                sleep(2)
            else:
                print_positions()
        else:
            pass


def command_inputs():
    while True:
        return input('-->')


def main():
    global stop_threads
    stop_threads = False
    x = threading.Thread(target=alarm_func)
    x.start()

    while True:
        with concurrent.futures.ThreadPoolExecutor() as command_executor:
            future = command_executor.submit(command_inputs)
            return_value = future.result()

            if return_value == 'quit':
                stop_threads = True
                sys.exit()

            elif return_value == 'help':
                print('Commands:')
                print('help - Provides a list of supported commands')
                print('change_time - Allows user to change the time of the update')
                print('quit - Stops the program')
            else:
                pass


if __name__ == '__main__':
    main()
