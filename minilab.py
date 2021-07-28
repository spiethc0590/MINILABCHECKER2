
from typing import NamedTuple
import requests
import json
import time
from pprint import pprint

#Meraki API Data
meraki_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "aeb3659a34994ccbf47bb70cac1b825a086db7d2"
}
meraki_base_url = "https://api.meraki.com/api/v1/"


#WEBEX API DATAs
webex_headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer NmFmYzExZDItOWE3OS00YmIxLTk2MjAtMWNhNWYxM2Y3N2M3OTUxMjdmY2MtMjUx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
                 }
webex_url = "https://webexapis.com/v1/messages"

def get_devices():
    networkdown = True
    org_ids= ["215332", "622622648483971160", "351024", "351028", "622622648483971212", "660903245316620328", "660903245316620327"]
    devices = []
    for org in org_ids:
        
        while networkdown == True:
            try:
                response = requests.request('GET', meraki_base_url + "organizations/"+ org +"/devices/statuses" , headers=meraki_headers, data = {})
                networkdown = False
            except:
                time.sleep(30)    
        devices.append(response.json())       
    return devices
   

def getoffline():
    net_devices = get_devices() 
    device_status = []
    count = 0
    while count < 7: 
        for devices in net_devices[count]:
            if "errors" in devices:
                pass
            elif devices["status"] == "offline": 
                device_status.append(devices["serial"])
    
        count += 1
    return device_status


def post_webex_message(SN):
    payload = json.dumps({
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNzY0NDNhYTAtMDdkYS0xMWViLWI4ZjEtMTU2MWFiZjc0NWM5",
    "text":SN + " Has been offline for 72 Hours  Please Investigate"
    })
    networkdown = True
    while networkdown == True:
            try:
                response = requests.request("POST", webex_url, headers=webex_headers, data=payload)
                networkdown = False
            except:
                time.sleep(30) 




if __name__ == "__main__":
    
 
    x = 0
    while x == 0:

        offline1 = getoffline()
        time.sleep(259200)
        offline2 = getoffline()

        for device in offline2:
            if device in offline1:
                post_webex_message(SN=device)

        offline1 == offline2   
        
             


   # roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNzY0NDNhYTAtMDdkYS0xMWViLWI4ZjEtMTU2MWFiZjc0NWM5"
   # mini lab checker id "Y2lzY29zcGFyazovL3VzL1JPT00vMjQ1MjdhZDAtZWU1OC0xMWViLTgzYTgtNWZlODFmNTA5NWVk"
   #webex token "NmFmYzExZDItOWE3OS00YmIxLTk2MjAtMWNhNWYxM2Y3N2M3OTUxMjdmY2MtMjUx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

   
