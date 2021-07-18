#!/usr/bin/python3
## The script asssumes that the person to be added with a permission to the repo is already a member in the organisation's github
## The daily rate limits for a repo setup by github is 50 using the API

import sys
import requests
import json

## Checking for parameters Oauth, org name, user permission to repo and username
if len(sys.argv) != 5:
	print("Usage:")
	print(f"{' '*4} {sys.argv[0]} [OAUTH_TOKEN] [ORGANIZATION_NAME] [PERMISSION] [USERNAME]")
	exit()

## Assigning arguments to global variables
GITHUB_OAUTH_TOKEN = str(sys.argv[1])
ORGS = str(sys.argv[2])
PERM = str(sys.argv[3])
USER = str(sys.argv[4])

## Request headers
headers = {
	"Authorization" : "token " + GITHUB_OAUTH_TOKEN,
	"Accept" : "application/vnd.github.v3+json"
}

## To check if Auth Token is correct
response = requests.get(f"https://api.github.com/orgs/{ORGS}",headers=headers)
if int(response.status_code) != 200:
	sys.stderr.write("OauthError: Authorization code could not be authenticated\n")
	sys.exit(1)

## To get response data of all repos in the organization
response = requests.get(f"https://api.github.com/orgs/{ORGS}/repos",headers=headers)
json_data = response.json()
repo_count = len(json_data)

print("Repo Name : Status")
## Applying the permission for the user to every repo
for i in range(repo_count):
	## Filter names of repos
	repo_name = json_data[i]["name"]
	print(repo_name , end=" : ")
	## Add user roles to repos
	response = requests.put(f"https://api.github.com/repos/{ORGS}/{repo_name}/collaborators/{USER}",data=json.dumps({"permission":PERM}),headers=headers)
	if int(response.status_code) == 201:
		print("Invitation sent")
	elif int(response.status_code) == 204:
		print("Already a collaborator")
	elif int(response.status_code) == 403:
		print("Forbidden")
	elif int(response.status_code) == 422:
		print("Validation Failed")
	else:
		sys.stderr.write("Failed\n")
		sys.exit(1)
print("Completed")
