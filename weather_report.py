import time
import sys
import Adafruit_DHT
from ISStreamer.Streamer import Streamer
streamer = Streamer(bucket_name="weather_report", bucket_key="REPORT", access_key="ist_-PLw5iSTr7Vju5PC7-Xo_FyMCo2f-keG")
while True:
    humidity , temperature = Adafruit_DHT.read_retry(11 ,4)
    print ("humidity = {}% ; temperature = {}C ".format(humidity,temperature )
    streamer.log("humidity", humidity)
    streamer.log("Temperature", temperature)
    sleep.time(1)       
