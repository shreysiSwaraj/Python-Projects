import requests
from requests.auth import HTTPBasicAuth
import json


url = "https://shreysiswaraj2000.atlassian.net/rest/api/3/issue"

# api_token is supposed to be assigned to a variable called API_TOKEN

auth = HTTPBasicAuth("shreysi.swaraj.2000@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10004"
    },
    "project": {
      "key": "SAM1"
    },
    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))