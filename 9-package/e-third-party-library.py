# First try install one by one then using requirements
# pip install psutil
# pip install -r requirements.txt

import os
import psutil

vcc = psutil.cpu_count()
print('Total number of CPUs :', vcc)

vcpu = psutil.cpu_percent()
print('Total CPUs utilized percentage :', vcpu, '%')

vram = psutil.virtual_memory()
print('Virtual memory :', vram)

disk = psutil.disk_usage(os.sep)
print('Disk :', disk)






import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&source=en&target=es"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "7bb16ac62bmsh978d27b9628aba1p16e7b4jsn6c919557883a",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)