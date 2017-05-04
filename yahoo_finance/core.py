""" This module contains the core functions needed to load, scrape and format
    quote data for the major indices from http://finance.yahoo.com/world-indices
"""
#!/usr/bin/env python

import urllib2
import re, json
from collections import OrderedDict

def load_data(location='http://finance.yahoo.com/world-indices',
              retry=5):
    """This function returns the contents of a webpage as a unicode string.
       On encountering timeout exceptions it will retry the specified number
       of times before giving up and rethrowing the exception
    """
    retry_count = 0
    done = False
    while (retry_count < retry) and not done:
        try:
            #yahoo_request = requests.get(location)
            yahoo_request = urllib2.urlopen(location)
            done = True
        except urllib2.HTTPError, e:
            retry_count += 1
            if retry_count >= retry:
                raise
    if yahoo_request.getcode() == 200:
        return yahoo_request.read()
    return ''

def scrape_world_indices_quote_data(pagedata):
    """This function scrapes the contents of a webpage and returns
        a dictionary representing the raw data of the major indices"""
    world_indices_re = re.compile(r'"YFinListStore":\{"lists":'
                                  r'\{"world_indices":\{("positions":\[.*?\])')
    quote_data_re = re.compile(r'"QuoteDataStore-Immutable":'
                               r'(\{"quoteData"\:.*?),"NavServiceStore"')

    indice_matches = world_indices_re.findall(pagedata)
    quote_data_matches = quote_data_re.findall(pagedata)

    world_indices = json.loads('{' + indice_matches[0] +'}')
    quote_data = json.loads(quote_data_matches[0])

    symbols = [w['symbol'] for w in world_indices['positions']]
    return OrderedDict((x, quote_data['quoteData'][x]) for x in symbols
                                      if x in quote_data['quoteData'])

def raw_data_to_dict(data):
    """This function constructs a dictionary from the raw scraped data
       containing the quoted data for the major indices
    """
    json_dict = OrderedDict()
    i = 1
    for symbol in data:
        json_dict[symbol] = OrderedDict()
        json_dict[symbol]['Id'] = i
        json_dict[symbol]['Symbol'] =\
                data[symbol]['symbol']
        json_dict[symbol]['Exchange'] =\
                data[symbol]['exchange']
        json_dict[symbol]['Exchange Full Name'] =\
                data[symbol]['fullExchangeName']
        json_dict[symbol]['Exchange Time Zone'] =\
                data[symbol]['exchangeTimezoneName']
        json_dict[symbol]['Regular Market Price'] =\
                data[symbol]['regularMarketPrice']['raw']
        json_dict[symbol]['Regular Market Volume'] =\
                data[symbol]['regularMarketVolume']['raw']
        json_dict[symbol]['Regular Market Change %'] =\
                data[symbol]['regularMarketChangePercent']['raw']
        json_dict[symbol]['Regular Market Time'] =\
                data[symbol]['regularMarketTime']['fmt']
        json_dict[symbol]['Market State'] =\
                data[symbol]['marketState']
        i += 1
    return json_dict
