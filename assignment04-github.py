# This program reads a file from a github repository, 
# then replaces all the instances of the text "Andrew" with my name; "Sarah"
# then any changes will be commited and pushed back to the repository. 

# Importing modules here
from github import Github
from config import config as cfg
import requests
import urllib.parse

# Setting token key here
apikey = cfg["githubkey"]

# Setting key to var g
g = Github(apikey)

# Setting dummy private repo for assignment
repo = g.get_repo("SarahMcN25/private_repo")
#print(repo.clone_url)

# Getting contents of text file from private github repo
filename = "andrew.txt"
file_info = repo.get_contents(filename)
url_of_file = file_info.download_url
#print(url_of_file) #debug

# Downloading url to make http request
response = requests.get(url_of_file)
contents_of_file = response.text
#print(contents_of_file) #debug

# Changing all occurences of Andrew to Sarah
new_contents = contents_of_file.replace("Andrew", "Sarah")
# print(new_contents)

# Committing and pushing changes to github
git_hub_response = repo.update_file(file_info.path,"updated by prog",
new_contents,file_info.sha)
print (git_hub_response)
