# This prog

# Import relevent modules
from ast import Pass
import requests
import json

# In cso page go down to API Data Query and click restful and copy url
# Making two urls to split the data in two
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Function to get dataset and save as json file
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

# Function to get dataset from API
def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

# Function to save funciton below to file
def getFormattedAsFile(dataset):
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file=fp)
  
# Function to return formated data as resutls dict
def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    # Count values as we go
    valuecount = 0
    # saving results as dict
    result = {}
    
    # for loop for first dimension
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        # get dim elemenet which is statistic, category and index and first element
        index = dimensions[currentId]["category"]["index"][dim0]
        # same to get label
        label0 = dimensions[currentId]["category"]["label"][index]
        # save resutls for each dim
        result[label0]={}
        
        print(label0)
        # for loop for second dimension
        # to get id, index and label
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            #print("\t",label1)
            result[label0][label1]={}
            
            # for loop for third dim
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                #print("\t\t",label2)
                result[label0][label1][label2]={}
           
                # for loop for fourth dim
                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    #print("\t\t\t",label, " ", values[valuecount])
                    result[label0][label1][label2][label3]= values[valuecount]
                    
                    # counting here 
                    valuecount+=1

        
    return result
    

# Calling main function to run prog
if __name__ == "__main__":
    getAllAsFile("FP001")
    getFormattedAsFile("FP001")