# Jenkins Pipeline to add User as GitHub Collaborator
This pipeline will add any user as a Collaborator in Github organization account.

## The 2 Stages of Pipeline -
| S.No | Stage Name | Stage Description |
|------|------------|--------------------|
| 1 | Build | Downloads the code from GitHub |
| 2 | Deploy | Add user as GitHub collaborator with the selected access type. |

## Prerequisites
- Jenkins should be Installed and configured.
- GitHub username.
- Set credentials in Jenkins to access GitHub repository.

## Pipeline Workflow
- withCredentials: For accessing the GitHub account, we need to setup the credentials in Jenkins.
- Downloads the pipeline and infrastructure code from github repository
