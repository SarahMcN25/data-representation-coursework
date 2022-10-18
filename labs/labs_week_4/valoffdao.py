# This prog pulls info from API reg propereties in county wicklow. 
# It saves it as a json file. 

# Importing modules to use
import urllib.parse
import requests
import json

url = "https://api.valoff.ie/api/Property/GetProperties"

# making parameters a dict so they can be edited easily
parameters_as_dict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG%,Use,FloorUse,Address,PublicationDate"   
}

# Funciton to retrieve info from API
def get_all():
    parameters = urllib.parse.urlencode(parameters_as_dict)
    #print (parameters)
    full_url = url + "?" + parameters
    response = requests.get(full_url)
    return response.json()

# Calling main function
if __name__ == "__main__":
    # Opening and storing info in json file
    with open("valoff.json", "wt") as fp:
        # formatting to json - in json file alt shift and f to format nicely
        print(json.dumps(get_all()), file=fp)