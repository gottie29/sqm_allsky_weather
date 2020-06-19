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



