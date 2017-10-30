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
quote_page = 'https://www.yelp.com/biz/smokes-poutinerie-berkeley'

# Using urllib2 to turn the URL into object
page = urllib2.urlopen(quote_page)

# Parse page using Beautiful Soup and store as object 'Soup'
soup = BeautifulSoup(page, 'html.parser')

# Find class name on site, take out div (Unwanted text/info) and get value
biz_name_class = soup.find('h1', attrs={'class': 'biz-page-title embossed-text-white shortenough'})
phone_num_class = soup.find('span', attrs={'class': 'biz-phone'})
address_class = soup.find('strong', attrs={'class': 'street-address'})


# Strip spaces and trailing
biz_name = biz_name_class.text.strip()
phone_num = str(phone_num_class.text.strip())

# Format due to Yelp fuckery
address = format_address(address_class)
# Convert from ASCII to string
biz_name = format_biz_name(biz_name)


# Prints number and address
print '{} \nPhone number: {} \nAddress: {}'.format(biz_name, phone_num, address)
