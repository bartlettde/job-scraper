import datetime


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
    print('What day would you like your update?')
    new_day = input('-->')
    formatted = new_day[:3]
    return formatted.capitalize()


def change_hour():
    print('What hour would you like your update?')
    print('Please just use the 24 hour format')
    new_hour = input('-->')
    return new_hour


def change_mins():
    print('What minute would you like your update?')
    new_min = input('-->')
    return new_min
