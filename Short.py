__author__ = 'supermacy'

import urllib2
import urllib
import requests
#import urllib.request as req
from bs4 import BeautifulSoup
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import time
import cookielib



url="http://infotsav.com/forex/calculation.php/"
currency_pair=input('Enter the currency pair:')
no_of_shares=input('Enter the no of shares you want to buy:')
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36 ',
                 "Cookie": "  PHPSESSID=4sabakna821bea0dbv5bf8b5a4","Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8"}

payload=urllib.urlencode({'laverage':'400','lots':'5','currency_pair':int(currency_pair),'recaptcha_response_field':'307','trantime':'12:00:05','REMOTE_ADDR':'14.139.240.251'})


import httplib, urllib
print "starting"
for i in range(0,no_of_shares):
    print i+1," shares brought"

    try:
            req = urllib2.Request(url,
                              headers = headers,
                              data = payload)
            f = urllib2.urlopen(req)
            #p = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(url)

            #print p.read()
    except:
            a=1

'''
conn = httplib.HTTPConnection("infotsav.com")
conn.request("POST", "/forex/calculation.php", payload, headers)
response = conn.getresponse()

print response
'''
