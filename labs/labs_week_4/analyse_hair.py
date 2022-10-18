# This prog uses function in another file to get data from API and return the total area

from webbrowser import get
from valoffdao import get_all

data = get_all()
total_area = 0

for entry in data:
    valuation_reports = entry["ValuationReport"]
    #print(valuation_reports) # debug
    for valuation_report in valuation_reports:
        #print(valuation_report) #debug
        #if valuation_report["FloorUse"] == "HAIR SALON":
            #print (valuation_report["Area"],"+", total_area,"=", end="")
        total_area += valuation_report["Area"]
            #print(total_area) # debug

print (total_area)