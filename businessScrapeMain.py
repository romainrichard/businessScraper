"""
Web Scraper to take input of a business name and return Address & Phone Number
"""

import urllib2

from bs4 import BeautifulSoup


def format_address(add):
    """
    Yelp makes addresses ugly, all this crap is to make them pretty.
    Takes a soup tag object
    Returns a String
    """
    addy = str(add)
    addy = addy.replace("<br/>", " ")
    addy = addy.split()

    del addy[0:3]
    del addy[-1]
    del addy[-1]

    addy = ' '.join(addy)

    return addy


def format_biz_name(bus):
    bus = bus.encode("utf-8")
    return bus

# ASKBUSINESS = raw_input('This program will return a '\
#                         'business Address and Phone Number from Yelp\n'\
#                         'Enter Business Name:\n')
# URL
QUOTE_PAGE = 'https://www.yelp.com/biz/smokes-poutinerie-berkeley'

# Using urllib2 to turn the URL into object
PAGE = urllib2.urlopen(QUOTE_PAGE)

# Parse page using Beautiful Soup and store as object 'Soup'
SOUP = BeautifulSoup(PAGE, 'html.parser')

# Find class name on site, take out div (Unwanted text/info) and get value
BIZ_NAME_CLASS = SOUP.find('h1', attrs={'class': 'biz-page-title embossed-text-white shortenough'})
PHONE_NUM_CLASS = SOUP.find('span', attrs={'class': 'biz-phone'})
ADDRESS_CLASS = SOUP.find('strong', attrs={'class': 'street-address'})


# Strip spaces and trailing
BIZ_NAME = BIZ_NAME_CLASS.text.strip()
PHONE_NUM = str(PHONE_NUM_CLASS.text.strip())

# Format due to Yelp fuckery
ADDRESS = format_address(ADDRESS_CLASS)
# Convert from ASCII to string
BIZ_NAME = format_biz_name(BIZ_NAME)


# Prints number and address
print '{} \nPhone number: {} \nAddress: {}'.format(BIZ_NAME, PHONE_NUM, ADDRESS)
