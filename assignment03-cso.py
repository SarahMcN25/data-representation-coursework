# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO.ie, 
# and stores it into a file called "cso.json"

# Import relevent modules
import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Funtion to get data from API
def get_file(dataset):
    response = requests.get(url)
    return response.json()

#Function to store API data to json file
def store_data(dataset):
    with open("cso.json", "wt") as fp:
        # calling other function to get data and storing in json format.
        print(json.dumps(get_file(dataset)), file=fp)

# call main method here
if __name__ == "__main__":
    #print(get_file) # debug
    # Note dataset name can be found at the end of the url above 
    print(store_data("FIQ02"))