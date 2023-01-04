# This script reads from the folder ../ontology_list
# This script downloads all the ontology files in the merged CSV locally.
import os
import re
import json
import csv
import requests


path = "../ontology_list/portal_download_urls/archivo.csv"
out_files = "../ontology_files/archivo/" 

problematic_uris = []

with open(path, mode='r') as in_file:
    data = list(csv.reader(in_file, delimiter=","))
    for elem in data:
        try:
            elem = elem[0] #it is read as a list of lists
            print("Downloading ",elem)
            response = requests.get(elem, timeout=30)
            file_name = elem
            file_name = file_name.replace("http://akswnc7.informatik.uni-leipzig.de/dstreitmatter/archivo/","")
            file_name = file_name.replace("https://akswnc7.informatik.uni-leipzig.de/dstreitmatter/archivo/","").replace('/','_')
            if response.status_code == 200:
                with open(out_files + file_name, "w") as f:
                    f.write(response.text)
        except Exception as e:
            print('Error downloading ', elem, str(e))
            problematic_uris.append(elem)

    print("Done!")
    print(f"{len(problematic_uris)} URIs were problematic")
    #print(problematic_uris)


