import requests
import json
import datetime
import re

date = datetime.datetime.now().strftime("%b %d")

map = {}

with open('/var/log/message', 'r') as f:
    for line in f.readlines:
        if date not in line:
            continue
        rec = line.split(' ')
        deviceName = rec[3]
        processId = re.findall(r'\[(.*?)\]', rec[4])
        processName = rec[4].split('[')[0]
        description = line.split(':')[-1]
        time = rec[2]+'00'+str(int(rec[2]+1)).zfill(2)+'00'
        
        key = (deviceName, processId, processName, description, time)
        if key not in map:
            map[key] = 1
        else:
            map[key] += 1

for key in map:
    data = {
        "deviceName" : key[0],
        "processId" : key[1],
        "processName" : key[2],
        "description" : key[3],
        "timeWindow" : key[4],
        "numberOfOccurrence" : map[key]
    }
    datalist.append(data)
 
headers = {'Content-Type': 'application/json'}
 
url = "https://foo.com/bar" 
response = requests.post(url, headers=headers, data = json.dumps(datalist))
 
print response.text