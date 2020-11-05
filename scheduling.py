import datetime


days_of_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}


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


def change_day():
    suitable = True

    print('What day would you like your update?')
    new_day = input('-->')

    for characters in new_day:
        if not characters.isdigit():
            suitable = True
        else:
            suitable = False

    if new_day.capitalize() in days_of_week and suitable:
        return new_day[:3]
    else:
        print('Sorry, we could not recognise this day. Please try again')
        change_day()


def change_hour():
    print('What hour would you like your update?')
    print('Please just use the 24 hour format')
    new_hour = input('-->')
    try:
        if 0 <= int(new_hour) <= 24:
            return new_hour
        else:
            print('Sorry, we could not recognise this value. Please try again')
            change_hour()
    except TypeError and ValueError:
        print('Sorry, we could not recognise this value. Please try again')
        change_hour()


def change_mins():
    print('What minute would you like your update?')
    new_min = input('-->')
    try:
        if 0 <= int(new_min) <= 60:
            return new_min
        else:
            print('Sorry, we could not recognise this value. Please try again')
            change_mins()
    except TypeError and ValueError:
        print('Sorry, we could not recognise this value. Please try again')
        change_mins()
