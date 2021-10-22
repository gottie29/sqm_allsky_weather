# sqm_allsky_weather
A allsky/sqm/weather /sensor station based on python

We are using an external server with a Influx Database and Grafana for visualiszation.
To use the DB functionality in our scripts you need a influx installation for raspberry pi

Installation Guides for InfluxDB:
---

https://pimylifeup.com/raspberry-pi-influxdb/<br>
https://simonhearne.com/2020/pi-influx-grafana/<br>


BME280 (bme280_influx.py)
-------------------------
BME280 is a sensor to read out the current temperature, humidity, pressure

This script read out the data and write data to a local file and/or to a influx database
To use the influx functionality you need the influxDBClient

Installation Guide for BOSCH-Sensor bme280:
https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/

ATTENTION: For the BME280 you need the i2c interface. Activate this in raspi-config

DHT22 (dht22-11_influx.py)
---
DHT22 is a sensor to read out/messure current temperature and humidity

This script read out the data and write data to a local file and/or to a influx database
To use the influx functionality you need the influxDBClient

PSUTIL (Processor Temp and more) (mypsutil.py)
---
To check the processor temperature and other internal values we use the mypsutil.py

Install-Guide: https://www.isendev.com/app/entry/39

Interface for ZWO and HQ cameras
--------------------------------
from Thomas Jacquin
Installation guide: https://github.com/thomasjacquin/allsky
