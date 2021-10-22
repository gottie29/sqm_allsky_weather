#!/usr/bin/python

import psutil
import time
import datetime
#from influxdb import InfluxDBClient

mydate = datetime.datetime.utcnow()
myTime = mydate.strftime('%Y-%m-%dT%H:%M:%SZ')

#### CPU
print('#### CPU ####')
cpu = psutil.cpu_times(False)
print("CPU ", cpu)

#### Memory
print('####MEMORY####')

mem = psutil.virtual_memory()
print("Memory ", mem)

mem = psutil.virtual_memory().total
print("Memory ", mem)

mem_avail = psutil.virtual_memory().available
print("Memory Available", mem_avail)

mem_perc = psutil.virtual_memory().percent
print("Memory ", mem_perc)

mem = psutil.virtual_memory().free
print("Memory ", mem)

#### DISK USAGE

print('####DISK USAGE####')

disk = psutil.disk_usage('/')
print("disk ", disk)

disk_total = psutil.disk_usage('/').total
print("disk ", float(disk_total/1048576))

disk_used = psutil.disk_usage('/').used
print("disk ", float(disk_used/1048576))

disk_free = psutil.disk_usage('/').free
print("disk ", float(disk_free/1048576))

disk_precent = psutil.disk_usage('/').percent
print("disk ", float(disk_precent))

#### Sensors

print('####DISK USAGE####')

sensors_temp = psutil.sensors_temperatures(False)
print("sensors ", sensors_temp)

print('####BOOT TIME####')

boottime = psutil.boot_time()
print("boottime ", boottime)
mytime = datetime.datetime.fromtimestamp(boottime).strftime("%d.%m.%Y %H:%M:%S")
print("boottime ", mytime)

json_body = [
{
  "measurement": "raspi_disk",
	"tags": {
	  "location": "Berlin",
	},
  "time": myTime,
  "fields": {
	  "disk_used": float(disk_used/1048576),
	  "disk_free": float(disk_free/1048576),
	  "disk_precent": float(disk_precent),
	  "memory_percent": float(mem_perc),
	  "raspi_onoff": 1
  }
}
]

#client = InfluxDBClient('Server','8086','user_name','pwd','database')
#client.write_points(json_body)  
