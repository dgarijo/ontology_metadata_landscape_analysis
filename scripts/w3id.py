# This script assumes https://github.com/perma-id/w3id.org/ is downloaded (git clone) locally
# at ../../ontology_landscape_data/w3id.org
import os
import re
import csv


pattern = r'RewriteRule (\^.*\$) (https?:\/\/[^\s]+\.(owl|ttl|nt|xml))'


def extract_ontology_links(dir_folder, dir_name):
    """
    Given a folder and a root path, this function iterates over that folder
    to extract all the htaccess files referring to an owl, ttl, nt or xml files.
    The w3id URI for each one is returned. Duplicates are removed.
    Note: this may return also TTL files from other projects.
    """
    link_list = []
    files = os.scandir(dir_folder)
    for entry in files:
        # get all htaccess files
        if entry.is_file() and ".htaccess" in entry.name:
            # print(entry.name)
            with open(entry, 'r') as f:
                contents_htaccess = f.read()
                matches = re.findall(pattern, contents_htaccess)
                for result in matches:
                    end_of_uri = result[0]
                    if "*" not in end_of_uri and "+" not in end_of_uri:
                        end_of_uri = end_of_uri.replace("^","").replace("$","").replace("?","").\
                            replace("\\","").replace("//","")
                        candidate_uri = dir_name+ os.sep+ end_of_uri
                        candidate_uri = "https://w3id.org" + candidate_uri
                        # small trick to remove those URIs with extensions when there is already a URI 
                        # that will do negotiation  
                        candidate_uri_no_ext = candidate_uri.replace(".ttl","").replace(".nt","").replace(".rdf","")
                        # we remove /people/ because these are not ontologies
                        if candidate_uri_no_ext not in link_list and "/people/" not in candidate_uri:
                            link_list.append(candidate_uri)
        elif entry.is_dir():
            link_list = link_list + extract_ontology_links(dir_folder + os.sep + entry.name, dir_name+ os.sep + entry.name)
                        
    return link_list

# Get the list of all files and directories
path = "../../ontology_landscape_data/w3id.org"
dir_list = os.scandir(path)

# we add the header 
final_list = ["vocabURI"]

#test1
#final_list = final_list + extract_ontology_links(path + os.sep+ "example", "example")
#test2
#final_list = final_list + extract_ontology_links(path + os.sep+ "okn", "okn")

final_list = final_list + extract_ontology_links(path, "")
#print(final_list)
print("List of URIs from w3id retrieved! Total size: ", str(len(final_list) - 1))
print("Printing to w3id.csv...")
with open('w3id.csv', mode='w') as out_file:
    csv.writer(out_file).writerows([uri] for uri in final_list)
print("Done!")

