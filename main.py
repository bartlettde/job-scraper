from time import sleep
import concurrent.futures
import threading
import sys
from getpass import getpass

import scraper  # contains all of the functions for scraping the different websites
import scheduling as sched  # contains all of the functions related to dates and times
import email_sender  # contains the functions for sending the email update

job_dict = {}
emailing_list = []


def command_inputs():
    while True:
        return input('-->')


def alarm_func(day: str, hour: int, mins: int):
    while True:
        if sched.get_day() == day.capitalize() and sched.get_hour() == hour and sched.get_min() == mins and sched.get_sec() == 10:
            output()
        elif stop_threads:
            break
        else:
            pass


def output():
    if len(emailing_list) == 0:
        print('There seems to be no address in the mailing list. Use the add recipient command to add addresses.')
        sleep(2)
        return
    else:
        print('Scraping')
        if not scraper.ideo_scraper():
            job_dict['Ideo'] = 'Failed to access page'
        else:
            job_dict['Ideo'] = scraper.ideo_scraper()

        if not scraper.frog_scraper():
            job_dict['Frog'] = 'Failed to access page'
        else:
            job_dict['Frog'] = scraper.frog_scraper()

        if not scraper.ammo_scraper():
            job_dict['Ammo'] = 'Failed to access page'
        else:
            job_dict['Ammo'] = scraper.ammo_scraper()

        email_sender.send_email(job_dict, sender, emailing_list, password)


def add_recipient():
    user_email = input('Please input the new email address:')
    emailing_list.append(user_email)
    print(user_email + ' successfully added')


def remove_recipient(email):
    if email in emailing_list:
        emailing_list.remove(email)
        print(email + 'successfully added')
    else:
        print('Address provided could not be found in list. Try again or use "show_list" command to see all of the '
              'items in the emailing list')


def main():
    day_of_alert = str(sched.change_day())
    hour_of_alert = int(sched.change_hour())
    min_of_alert = int(sched.change_mins())

    add_recipient()

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

            elif return_value == 'add_to_list':
                add_recipient()

            elif return_value == 'show_list':
                for i in emailing_list:
                    print(i)

            elif return_value == 'remove_from_list':
                user_email = input('Please input the address you would like to remove:')
                remove_recipient(user_email)

            else:
                print('Command not supported, please try again or type "help" for a list of supported commands')
                pass


if __name__ == '__main__':
    global sender
    global password

    sender = input('Please insert the email address you would like to send the email from:')
    password = getpass('Please insert the password for the email address:')

    main()
