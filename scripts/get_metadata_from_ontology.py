# This script assumes https://github.com/perma-id/w3id.org/ is downloaded (git clone) locally
# at ../../ontology_landscape_data/w3id.org
import os
import sys
import re
from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery

# Given a folder, this method will traverse all ontologies and generate metadata file per ontology 
# including only the annotations for all ontos/concepts schemes found
# If there is no ontology or concept scheme, the program produces an error

def extract_ontology_annotations(ontology_path, out_path): 
    try:   
        onto = Graph()
        onto.parse(ontology_path, format="turtle")    
    except:
        try:
            print("Could not parse ontology in ttl. Trying in xml...")
            onto.parse(ontology_path, format="xml")    
        except:
            print("Could not load the ontology in rdf/xml or turte.")
            return
    
    q = prepareQuery('''
      SELECT ?s ?p ?o WHERE {
       {  
       ?s a <http://www.w3.org/2002/07/owl#Ontology>.
       }
       UNION
       {
       ?s a <http://www.w3.org/2004/02/skos/core#ConceptScheme>
       }
       ?s ?p ?o 
      }
    ''')
    summary = Graph()
    PROV = Namespace("http://www.w3.org/ns/prov#")
    onto_uri = ""
    for r in onto.query(q):
        if (r.s != onto_uri):
            summary.add((r.s,PROV.hadPrimarySource,Literal(ontology_path)))    
        summary.add((r.s,r.p,r.o))
    # add the source URI
    # print(summary.serialize(format="ttl"))
    # serialize in TTL per file if triples are found
    try:
        if len(summary):
            out_file = os.path.join(out_path, os.path.basename(ontology_path))
            print("Saving RDF data to " + str(out_file))
            with open(out_file, "wb") as out_f:
                out_f.write(summary.serialize(format="ttl", encoding="UTF-8"))
        else:
            #save in error file
            print("Could not extract metadata from %s", ontology_path )
    except Exception as e:
        print("Error while saving RDF results "+str(e))


# main script
#directory = sys.argv[1]
#for filename in os.listdir(directory):
#    path = os.path.join(directory, filename)
#    if os.path.isfile(path):
#        print(filename)


# Tests
#extract_ontology_annotations("../ontology_files/wild/w3id.org_example.ttl",".")
#extract_ontology_annotations("../ontology_files/bioportal/M4M19-SUBS.owl",".")



