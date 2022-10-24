# Based on week 5 labs for data rep. 

from github import Github
from config import config as cfg
import requests
import urllib.parse

apikey = cfg["githubkey"]

#use own key
g = Github(apikey)

# Prints a list of public repos/and selected private one. 
#for repo in g.get_user().get_repos():
#    print(repo.name)

# clones and prints repo url
repo = g.get_repo("SarahMcN25/private_repo")
#print(repo.clone_url)

# getting contents of private repo text file
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# downloading url to make http request
response = requests.get(urlOfFile)
contentsOfFile = response.text
#print(contentsOfFile)

# adding more content to private file
newContents = contentsOfFile + "adding more stuff \n"
#print(newContents)

# update the contents to github here 
gitHubResponse = repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print (gitHubResponse)