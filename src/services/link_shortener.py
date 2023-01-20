from pyshorteners import Shortener

def shorten_application_link(shortener, application_link):
    short_url = shortener.short(application_link)
    return short_url