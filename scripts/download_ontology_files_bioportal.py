# This script reads from the folder ../ontology_list
# This script downloads all the ontology files in the target CSV using an authentication header for that portal.
import os
import re
import json
import csv
import requests


path = "../ontology_list/portal_download_urls/ecoportal.csv"
out_files = "../ontology_files/ecoportal/" 
#url = "https://data.bioontology.org/ontologies/"
url= "https://data.ecoportal.lifewatch.eu/ontologies/"
api_key = "YOUR_KEY_GOES_HERE"

problematic_uris = []

with open(path, mode='r') as in_file:
    data = list(csv.reader(in_file, delimiter=","))
    existing_files = os.scandir(out_files)
    existing_files = [entry.name for entry in existing_files]
    for elem in data:
        try:
            elem = elem[0] #it is read as a list of lists
            file_name = elem.replace(url,"").replace("download","").replace("/","")
            file_name = file_name + ".owl"
            if file_name not in existing_files:
                print("Downloading ",elem)
                headers = {
                        'Authorization': "apikey token="+api_key
                    }
                response = requests.get(elem, headers=headers, allow_redirects=True, timeout=10)
                if response.status_code == 200:
                    with open(out_files + file_name, "w") as f:
                        f.write(response.text)
            else:
                print(f'File {file_name} already downloaded!')
        except Exception as e:
            print('Error downloading ', elem, str(e))
            problematic_uris.append(elem)

    print("Done!")
    print(f"{len(problematic_uris)} URIs were problematic")
    #print(problematic_uris)


