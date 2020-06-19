#!/usr/bin/python

########################################################
# DHT22 / DHT11 - Temperature and Humidity by Adafruit
# 
# Author: Stefan Gotthold / Bob Andrews
#         gottie29 / bobandrews23
#
# Date:   21/06/2020
#
# Version: v001
#
########################################################

import Adafruit_DHT
import time
import datetime
from influxdb import InfluxDBClient

# InfluxDB settings
# DB settings
HOST = ''
PORT = ''
USER = ''
PASSWORD = ''
DBNAME = ''

# File settings


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

# sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT22

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
# pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 10

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  mydate = datetime.datetime.utcnow()
  myTime = mydate.strftime('%Y-%m-%dT%H:%M:%SZ')
      
  json_body = [
  {
    "measurement": "dht22",
    "tags": {
      "location": "Berlin",
      },
    "time": myTime,
    "fields": {
      "temp": float(temperature),
      "hum": float(humidity)
    }
  }
  ]

  client = InfluxDBClient(HOST,PORT,USER,PASSWORD,DBNAME)
  client.write_points(json_body)   
    
    
else:
    print('Failed to get reading. Try again!')
