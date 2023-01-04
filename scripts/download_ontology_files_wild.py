# This script reads from the folder ../ontology_list
# This script downloads all the ontology files in the merged CSV locally.
import os
import re
import json
import csv
import requests


path = "../ontology_list/wild_uris/wild_merged_no_portals.csv"
out_files = "../ontology_files/wild/" 

problematic_uris = []

with open(path, mode='r') as in_file:
    data = list(csv.reader(in_file, delimiter=","))
    for elem in data:
        try:
            elem = elem[0] #it is read as a list of lists.
            print(elem)
            for serialization in ['text/turtle', 'application/rdf+xml', 'application/n-triples', 'application/ld+json']:
                print(f'Attempting to download {elem} in {serialization}')
                headers = {
                    'Accept': serialization
                }
                response = requests.get(elem, headers=headers, allow_redirects=True, timeout=10)
                file_name = elem
                if file_name.endswith("#") or file_name.endswith("/"):
                    file_name = file_name[:len(file_name)-1] 
                file_name = file_name.replace("https://","").replace("http://","").replace('/','_')
                if response.status_code == 200:
                    if serialization == 'text/turtle' and ".ttl" not in file_name:
                        file_name += ".ttl"
                    elif serialization == 'application/rdf+xml' and ".rdf" not in file_name:
                        file_name += ".rdf"
                    elif serialization == 'application/n-triples' and ".nt" not in file_name:
                        file_name += ".nt"
                    elif serialization == 'application/ld+json' and ".json" not in file_name:
                        file_name += ".jsonld"
                    with open(out_files + file_name, "w") as f:
                        f.write(response.text)
                        break 
        except Exception as e:
            print('Error downloading ', elem, str(e))
            problematic_uris.append(elem)

    print("Done!")
    print(f"{len(problematic_uris)} URIs were problematic")
    print(problematic_uris)


