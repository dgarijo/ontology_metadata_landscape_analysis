# This script reads from the folder ../ontology_list
import os
import re
import json
import csv


path = "../ontology_list/portals"


files = os.scandir(path)
for entry in files:
    full_list = []
    if entry.name.endswith(".json"):
        print(entry.name)
        with open(entry, mode='r') as in_file:
            data = json.load(in_file)
            for elem in data:
                #print(elem)
                try:
                    if "links" in elem.keys():
                        full_list.append(elem["links"]["download"])
                except:
                    pass

            #Print to file
            print(f'Printing entry {entry.name} to file...')
            with open(entry.name+'.csv', mode='w') as out_file:
                csv.writer(out_file ,quoting=csv.QUOTE_NONE, quotechar='').writerows([uri] for uri in full_list)
            print("Done!")


