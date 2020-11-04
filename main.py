from time import sleep
import concurrent.futures
import threading
import sys

import scraper  # contains all of the functions for scraping the different websites
import scheduling as sched  # contains al of the functions related to dates and times

job_dict = {}


def command_inputs():
    while True:
        return input('-->')


def alarm_func(day: str, hour: int, mins: int):
    print('alarm func called')
    while True:
        if sched.get_day() == day.capitalize() and sched.get_hour() == hour and sched.get_min() == mins and sched.get_sec() == 10:
            print('working')
            output()
        elif stop_threads:
            break
        else:
            pass


def output():
    if not scraper.ideo_scraper():
        job_dict['Ideo'] = 'Failed to load'
    else:
        job_dict['Ideo'] = scraper.ideo_scraper()

    if not scraper.frog_scraper():
        job_dict['Frog'] = 'Failed to load'
    else:
        job_dict['Frog'] = scraper.frog_scraper()

    if not scraper.ammo_scraper():
        job_dict['Ammo'] = 'Failed to load'
    else:
        job_dict['Ammo'] = scraper.ammo_scraper()

    for x, y in job_dict.items():
        print(x, y)
    sleep(2)


def main():
    day_of_alert = str(sched.change_day())
    hour_of_alert = int(sched.change_hour())
    min_of_alert = int(sched.change_mins())

    global stop_threads
    stop_threads = False

    x = threading.Thread(target=alarm_func, args=(day_of_alert, hour_of_alert, min_of_alert))
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
                print('test - Sends an update immediately')
                print('change_time - Allows user to change the time of the update')
                print('quit - Stops the program')

            elif return_value == 'change_time':
                stop_threads = True
                main()

            elif return_value == 'test':
                output()

            else:
                print('Command not supported, please try again or type "help" for a list of supported commands')
                pass


if __name__ == '__main__':
    main()
