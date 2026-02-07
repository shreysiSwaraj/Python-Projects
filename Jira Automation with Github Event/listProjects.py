import requests
from requests.auth import HTTPBasicAuth
import json

##Jira projects have been named as Spaces, so do not get confused
url = "https://shreysiswaraj2000.atlassian.net//rest/api/3/project"

# api_token is supposed to be assigned to a variable called API_TOKEN

auth = HTTPBasicAuth("shreysi.swaraj.2000@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output = json .loads(response.text)

#print(output)
for item in output:
    print(f"Project name : {item['name']}")
# name = output[0]["name"]
# print(name)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))