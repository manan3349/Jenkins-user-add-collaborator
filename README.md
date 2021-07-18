# Jenkins Pipeline to add User as GitHub Collaborator
This pipeline will add any user as a Collaborator in Github organization account.

## The 2 Stages of Pipeline -
| S.No | Stage Name | Stage Description |
|------|------------|--------------------|
| 1 | Build | Downloads the code from GitHub |
| 2 | Deploy | Add user as GitHub collaborator with the selected access type. |

## Prerequisites
- Jenkins should be Installed and configured.
- Install pipeline plugin in Jenkins.
- GitHub username.
- Set credentials in Jenkins to access GitHub repository.

## Pipeline Workflow
- withCredentials: For accessing the GitHub account, we need to setup the credentials in Jenkins.
- Downloads the pipeline and code from github repository.
- Add a GitHub collaborator with the following permissions selected by the user.

## Variables Used
### Jenkins Parameters:
- `access_type` - It is a choice parameter which gives a dropdown to select the particular permission.
- `USER_NAME` - It is a string parameter which asks for username to add.
- `ORG_NAME` - It is a string parameter which asks for Organization name.

## How to use
- Copy the Pipeline code in your Jenkins job.
- Set the credentials of GitHub in Jenkins.
- Replace the `withCredentials` block with your own credentials.
- Put Github_access.py in your GitHub account whose credentials you setted up in Jenkins by this, Jenkins will download the code first in the server.
- Deploy stage will run the python code and add user as a GitHub collaborator.

### Further Reference and Contact 
##### Feel free to Contact for any issue!!

<a href="https://www.linkedin.com/in/mananjainn/" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /> </a>

