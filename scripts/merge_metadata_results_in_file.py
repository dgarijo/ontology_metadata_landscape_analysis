# This script takes all the results from the folder 
# "metadata results" and merges them in a single file.
import os
import sys
import re
from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery


def process_folder(folder_path,out_file):
    onto = Graph()
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        print("loading: ",path)
        if os.path.isfile(path):            
            onto.parse(path, format="turtle")     
    print("Saving RDF data to " + str(out_file))
    with open(out_file, "wb") as out_f:
        out_f.write(onto.serialize(format="ttl", encoding="UTF-8"))       
 


folder_to_process = "metadata_results"
out = "metadata_results.ttl"
if not os.path.isdir(folder_to_process):
    os.mkdir(folder_to_process)
print("merging all TTL files in one TTL file for querying")
process_folder(folder_to_process, out)
print("Done")
