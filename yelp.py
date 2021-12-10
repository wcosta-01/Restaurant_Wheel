import argparse
import json
import pprint
import requests
import sys
import urllib

API_Key = 'Xmg8Xh7IcJTDh9YxXh_-F07uprqcEn7LKfcctQDx_GUNcJxCx02Vx1m3mfv0NzB79R8kCYEB3AiNGKJ63ZF0cpYIou5gafX9WkkMOFswmN85lShOP0GcikTP3VCVYXYx'
API_Host = 'https://api.yelp.com'
Search_Path = '/v3/businesses/search'

Term = 'seafood'
Location = 'NYC'
Search_Limit = 5
Radius = 50

def request(api_key, url_params=None):

    #querying information, via search method variables
    url_params = url_params or {}
    url = API_Host + Search_Path
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()



def search(api_key, term, location):

    #query with imported variables
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': Search_Limit
    }

    return request(API_Key, url_params=url_params)

data_dict = search(API_Key, Term, Location)
print(data_dict)    
