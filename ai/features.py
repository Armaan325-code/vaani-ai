from datetime import datetime


def get_time():
    return datetime.now().strftime("Current time is %I:%M %p")


def get_date():
    return datetime.now().strftime("Today is %d %B %Y")