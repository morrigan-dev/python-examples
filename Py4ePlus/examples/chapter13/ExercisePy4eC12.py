'''
Created on 17.03.2020

Hier werden die Aufgaben aus dem Kurs 'Python for everbody - Kapitel 13' gelöst.

@author: morrigan
@see: https://www.py4e.com/html3/13-web
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

from examples import print_exercise
from examples import print_header

print_header("Python for everybody - Kapitel 13 - Exercises")

# Exercise 1
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    params = dict()
    params["address"] = address
    if api_key is not False: params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    address_components = js['results'][0]['address_components']
    for comp in address_components:
        print(js['results'][0]['address_components'])

    location = js['results'][0]['formatted_address']
    print(location)
