
import argparse
import webbrowser
import random
import json
import pprint
import requests
import sys
import urllib

API_Key = 'Xmg8Xh7IcJTDh9YxXh_-F07uprqcEn7LKfcctQDx_GUNcJxCx02Vx1m3mfv0NzB79R8kCYEB3AiNGKJ63ZF0cpYIou5gafX9WkkMOFswmN85lShOP0GcikTP3VCVYXYx'
API_Host = 'https://api.yelp.com'
Search_Path = '/v3/businesses/search'

Search_Limit = 50 #a decent number to work with

#reading in from shell command
Location = sys.argv[1]
Radius = sys.argv[2]

#Radius mile to meter conversion
Radius = float(Radius) * 1609.34
Radius = round(Radius) #query requires int

if Radius > 40000: #max
    Radius = 40000
elif Radius < 1609: #approx. 1 mile
    Radius = 1609

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



def search(api_key, location):

    #query with imported variables
    url_params = {
        'location': location.replace(' ', '+'),
        'limit': Search_Limit,
       'radius' : Radius
    }

    return request(API_Key, url_params=url_params)

data = search(API_Key, Location) 
data_dict = {}

#json-to-dictionary
num = 0
for business in data['businesses']:
    data_dict[num] = business["url"]
    num += 1

#random web browsing
rand_int = random.randint(0, len(data_dict) - 1) 
webbrowser.open(data_dict[rand_int])

