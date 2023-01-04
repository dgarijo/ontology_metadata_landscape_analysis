# This script reads from the folder ../ontology_list
import os
import re
import csv


path = "../ontology_list/wild_uris"

full_list = []
files = os.scandir(path)
for entry in files:
    if entry.name.endswith(".csv"):
        print(entry.name)
        with open(entry, mode='r') as in_file:
            data = list(csv.reader(in_file, delimiter=","))
            full_list += [d[0] for d in data]
            print("#Ontos added to list: ", str(len(data)))
print("#Ontos in list (before duplicate removal): ", str(len(full_list)))
#remove_duplicates
full_list = [*set(full_list)]

# remove "vocabURI", the header
full_list.remove("vocabURI")

# if the same URI is added with trailing slash and hash, keep only one
# version
full_list = [list_item for list_item in full_list if list_item[:len(list_item)-1] not in full_list]

full_list.sort()

print("#Ontos in list (after duplicate removal): ", str(len(full_list)))

#Print to file
print("Printing to merged.csv...")
with open('merged.csv', mode='w') as out_file:
    csv.writer(out_file ,quoting=csv.QUOTE_NONE, quotechar='').writerows([uri] for uri in full_list)
print("Done!")


