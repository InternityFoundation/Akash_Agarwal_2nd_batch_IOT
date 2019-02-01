import os
import time
import sys
import Adafruit_DHT
import urllib2

myAPI = "6P5KO9L4BZM5ZV4X"
myDelay = 15 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
    humidity , temperature = Adafruit_DHT.read_retry(11 ,4)
    print ("humidity = {}% ; temperature = {}C ".format(humidity,temperature))
 
 f = urllib2.urlopen(baseURL + "&field2=%s" % int(temperature))
 print f.read()
