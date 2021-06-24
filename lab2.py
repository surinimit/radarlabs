import json
from datetime import datetime
from datetime import date
import os

#Pprerequisite: install trivy and docker as well before you execute the script
#input for the code image to pull. 

docker_image = input("Please enter the docker image that you wish to scan: ")
os.system(f'docker pull {docker_image}')
os.system(f"trivy -q -severity HIGH --format=json {docker_image} |  jq | less > ./lab2.json")

# Code to Parse the Json File generated with vulnerability data
with open('lab2.json') as d:
    dicdata = json.load(d)
    for data in dicdata[0]["Vulnerabilities"]:
        if "PublishedDate" in data:
            raw_date = data["PublishedDate"]
            modified_date = raw_date[0:10]
            date_time_obj = datetime.strptime(modified_date, "%Y-%m-%d")
            todays_date = datetime.today()
            delta = todays_date - date_time_obj
            str1 =delta.days
            if(int(str1)> 90):
                print(data["VulnerabilityID"], " ", data["Severity"], " ", " This vulnerability is rated as Low based on SLA")
            if(int(str1)>= 60 and int(str1)<90):
                print(data["VulnerabilityID"], " ", data["Severity"], " ", " This vulnerability is rated as Medium based on SLA")
            if(int(str1)>= 30 and int(str1)<60):
                print(data["VulnerabilityID"], " ", data["Severity"], " ", " This vulnerability is rated as High based on SLA")
            if(int(str1)>= 1 and int(str1)<30):
                print(data["VulnerabilityID"], " ", data["Severity"], " ", "  This vulnerability is rated as Critical based on SLA")
            
os.remove("lab2.json")      
    
   
