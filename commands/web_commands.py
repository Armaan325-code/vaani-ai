import webbrowser


def open_google():
    webbrowser.open("https://google.com")


def open_youtube():
    webbrowser.open("https://youtube.com")


def open_github():
    webbrowser.open("https://github.com")


def open_gmail():
    webbrowser.open("https://mail.google.com")


def search_google(query):
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )


def search_youtube(query):
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )