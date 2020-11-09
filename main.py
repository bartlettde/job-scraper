from time import sleep
import concurrent.futures
import threading
import sys
from getpass import getpass
try:
    import pyfiglet
    pyfig_lib = True
except ImportError:
    pyfig_lib = False

import scraper  # contains all of the functions for scraping the different websites
import scheduling as sched  # contains all of the functions related to dates and times
import email_sender  # contains the functions for sending the email update

job_dict = {}
emailing_list = []


def sender():
    global sender_var
    sender_var = input('Please insert the email address you would like to send the update emails from:')


def password():
    global password_var
    password_var = getpass('Please insert the password for the email address:')


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

        job_dict['Ideo'] = scraper.ideo_scraper()
        job_dict['Frog'] = scraper.frog_scraper()
        job_dict['Ammo'] = scraper.ammo_scraper()

        email_sender.send_email(job_dict, sender_var, emailing_list, password_var)


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


def help_command():
    print('Commands:')
    print('help - Provides a list of supported commands')
    print('test - Sends an update immediately')
    print('change_time - Allows user to change the time of the update')
    print('add_to_list - Allows user to insert a new email address into the emailing list')
    print('show_list - Allows user to view the entire emailing list')
    print('remove_from_list - Allows user to remove a specific email from the list')
    print('change_email - Allows user to change the sender email address')
    print('change_password - Allows users to change their password')
    print('quit - Stops the program')


def main():
    day_of_alert = str(sched.change_day())
    hour_of_alert = int(sched.change_hour())
    min_of_alert = int(sched.change_mins())

    add_recipient()

    global stop_threads
    stop_threads = False

    help_command()

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
                help_command()

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

            elif return_value == 'change_email':
                sender()

            elif return_value == 'change_password':
                password()

            else:
                print('Command not supported, please try again or type "help" for a list of supported commands')
                pass


if __name__ == '__main__':
    print('Welcome to...')
    if pyfig_lib:
        bob_jot = pyfiglet.Figlet(font='larry3d')
        print(bob_jot.renderText('Bob Jot !'))
    else:
        print('Bob Jot!')
    print('The Web Scraping, Job Bot')

    sender()
    password()

    main()
