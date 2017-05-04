from yahoo_finance import core
from collections import OrderedDict
import json, os
from nose.tools import *


def test_scrape_function():
    indices = ['^GSPC','^DJI','^IXIC','^NYA','^XAX','^BATSK',
                '^RUT','^VIX','^FTSE','^GDAXI','^FCHI','^STOXX50E','^N100',
                '^BFX','MICEXINDEXCF.ME','^N225','^HSI','000001.SS','^STI',
                '^AXJO','^AORD','^BSESN','^JKSE','^KLSE','^NZ50','^KS11',
                '^TWII','^GSPTSE','^BVSP','^MXX','^IPSA','^MERV','^TA100',
                '^CASE30','JN0U.FGI']
    testdata_file = os.path.join(os.path.dirname(__file__), 'sample_pagedata.html')
    with open(testdata_file, 'r') as f:
        pagedata = f.read()
    raw_scraped_data = core.scrape_world_indices_quote_data(pagedata)
    # There are 35 major indices
    assert len(raw_scraped_data) == 35
    assert raw_scraped_data.keys() == indices
        
def test_raw_data_to_dict():
    testdata_file = os.path.join(os.path.dirname(__file__), 'sample_pagedata.html')
    with open(testdata_file, 'r') as f:
        pagedata = f.read()
    raw_scrapped_data = core.scrape_world_indices_quote_data(pagedata)
    formatted_data = core.raw_data_to_dict(raw_scrapped_data)
    assert len(formatted_data) == 35

@raises(ValueError)    
def test_malformed_url_pageload():
    core.load_data(location='nonesuch')

