import requests

response = requests.get("https://api.github.com/users/shreysiSwaraj/repos")

projects = response.json()
#print(projects)

for project in projects:
    print(f"Project Name : {project['name']} Project URL : {project['url']}" )