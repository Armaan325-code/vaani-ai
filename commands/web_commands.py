import webbrowser

GOOGLE_URL = "https://google.com"
YOUTUBE_URL = "https://youtube.com"
GITHUB_URL = "https://github.com"
GMAIL_URL = "https://mail.google.com"


def open_google():
    webbrowser.open(GOOGLE_URL)


def open_youtube():
    webbrowser.open(YOUTUBE_URL)


def open_github():
    webbrowser.open(GITHUB_URL)


def open_gmail():
    webbrowser.open(GMAIL_URL)


def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")


def search_youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")