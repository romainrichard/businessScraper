"""
Web Scraper to take input of a business name and return Address & Phone Number
Asks User for business name
Uses this to search Yelp, gets link of actual business from search results.
Goes to URL of actual business page
Scrapes Address and Phone Number

If I look at this in a year and this doc string helps me understand what i did , give Jesse 25 cents
(Even though he is currently suffering from male pattern Hunter S. Thompson-ness)
"""

import re

import urllib2

from bs4 import BeautifulSoup


def format_address(add):
    """
    Takes BS tag object, converts to string. Replaces <br> tags with nothing.
    Then, uses Regex to remove everything in between tags. (Non-text)
    Finally, strips the address of whitespace.
    :param add: beautiful soup object representing address
    :return: Nicely formatted String Address
    """
    addy = str(add)
    addy = addy.replace("<br/>", " ")
    addy = re.sub(r'<.+?>', '', addy)
    addy = addy.strip()
    return addy


def format_search_link(lnk):
    """
    Searches for first HTML tag starting with "a"
    Take HTML class/tag of first search Result
    Return only the end of URL that you need
    """
    format_biz_link = lnk.find('a')
    return format_biz_link.attrs['href']


def format_uni_to_string(bus):
    """
    As business names can have apostrophes and such, This converts them.
    Takes ASCII business name
    Returns String business name
    """
    bus = bus.encode("utf-8")
    return bus


# Main Yelp URL
YELP_INDEX = 'https://www.yelp.com'

# Code Below - Getting Business Name from User, Searching this on Yelp

# Yelp search Link, to be appended with user input
SEARCH_YELP = 'https://www.yelp.com/search?find_desc='

ASK_BUSINESS = raw_input('\nThis program will return a'
                         'business Address and Phone Number from Yelp!\n'
                         '\nEnter Business Name:\n')


# Append user inputted business so Yelp Search link
SEARCH_YELP += ASK_BUSINESS
SEARCH_YELP = SEARCH_YELP.replace(' ', '+')

# Using urllib2 to turn the search URL into object
SEARCH_PAGE = urllib2.urlopen(SEARCH_YELP)

# Parse search page using Beautiful Soup and store as object 'SEARCHED'
SEARCH_RESULT_PAGE = BeautifulSoup(SEARCH_PAGE, 'html.parser')


# Find correct business on Search Results page
SEARCHED_BIZ_LINK_CLASS = SEARCH_RESULT_PAGE.find('span', attrs={'class': 'indexed-biz-name'})
SEARCHED_BIZ_LINK_CLASS = format_search_link(SEARCHED_BIZ_LINK_CLASS)

FULL_URL = YELP_INDEX + SEARCHED_BIZ_LINK_CLASS

# URL - This is how you would ordinarily use a URL with BS
# QUOTE_PAGE = 'https://www.yelp.com/biz/equinox-berkeley-berkeley-2?osq=gym'

# Code Below - Now we have the actual business URL. We now scrape from this page


# Using urllib2 to turn the URL into object
PAGE = urllib2.urlopen(FULL_URL)

# Parse page using Beautiful Soup and store as object 'Soup'
SOUP = BeautifulSoup(PAGE, 'html.parser')

# Find class name on site, take out div (Unwanted text/info) and get value
BIZ_NAME_CLASS = SOUP.h1
PHONE_NUM_CLASS = SOUP.find('span', attrs={'class': 'biz-phone'})
ADDRESS_CLASS = SOUP.find('strong', attrs={'class': 'street-address'})

# Strip spaces and trailing
BIZ_NAME = BIZ_NAME_CLASS.text.strip()
PHONE_NUM = PHONE_NUM_CLASS.text.strip()

# Format to give pretty address
FORMATTED_ADDRESS = format_address(ADDRESS_CLASS)

# Convert from ASCII to string
BIZ_NAME = format_uni_to_string(BIZ_NAME)
PHONE_NUM = format_uni_to_string(PHONE_NUM)
ADDRESS = format_uni_to_string(FORMATTED_ADDRESS)

# Prints number and address
print 'Business name: {} \nPhone number: {} \nAddress: {}'.format(BIZ_NAME, PHONE_NUM, ADDRESS)
