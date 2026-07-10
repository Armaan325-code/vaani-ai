from datetime import datetime


def get_time():
    now = datetime.now()
    return now.strftime("Current time is %I:%M %p")


def get_date():
    today = datetime.now()
    return today.strftime("Today is %d %B %Y")