import os

def open_notepad():
    os.system("notepad")

def open_calculator():
    os.system("calc")

def open_paint():
    os.system("mspaint")

def open_cmd():
    os.system("start cmd")

def open_explorer():
    os.system("explorer")

def open_downloads():
    os.system(f'explorer "{os.path.expanduser("~/Downloads")}"')