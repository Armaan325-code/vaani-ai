import psutil

def get_battery():
    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is not available."

    percent = battery.percent

    if battery.power_plugged:
        status = "charging"
    else:
        status = "not charging"

    return f"Battery is {percent} percent and it is {status}."
