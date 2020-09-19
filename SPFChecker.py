import csv
from SPF2IP import SPF2IP
Domains = []
Success = []

with open('pressidium-primary-domains.csv', newline='') as csvfile:
     domainreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in domainreader:
         #print(row[1])
         Domains.append(row[1])

itemCount = -1
for item in Domains:
    itemCount += 1
    if itemCount == 0:
        pass
    else:
        lookup = SPF2IP(item)

        try:
            records = lookup.GetSPFArray(item)
        except:
            pass

        #print(itemCount)
        #print(item)
        #print(records)
        if records != []:
            #print("True")
            Success.append(str(itemCount) + ",True," + item + "," + str(records))
        else:
            #print("False")
            Success.append(str(itemCount) + ",False," + item + "," + str(records))

        #for record in records:
            #print(record)

for attempt in Success:
    print(attempt)

import numpy as np
np.savetxt("SPF_Records.csv", Success, delimiter=",", fmt='%s', header="Number,Has SPF,Domain,Record --->")
