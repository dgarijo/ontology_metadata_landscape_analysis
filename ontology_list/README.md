## List of ontologies

This folder contains the main sources used for our analysis, futher described below:

* wild_uris/list_mp.csv: list with nearly 3000 ontology URIs collected by a student. It includes LOV and part of w3id among others.
* wild_uris/lov.csv: vocabularies included in the Linked Open Vocabularies repository.
* wild_uris/w3id.csv: vocabularies included in w3id.org. See the script in /scripts/w3id.py to find how the list is generated.
* wild_uris/ontoology.csv: vocabularies published with [OnToology](https://ontoology.linkeddata.es/). From the results additional redundant URIs have been removed.
* wild_merged_no_portals.csv: a merged list with ontology URIs from all previous sources except ontologies in any bio portal istances. Duplicates are removed.

Portals are separated from all the rest, as each one needs an API KEY to download each ontology. These are the portals that have been analyzed:
* bioportal.csv: list of download URLs for the ontologies in [bioportal](http://data.bioontology.org/documentation).
* industry.csv: list of download URLs for the ontologies in [industry portal](http://data.industryportal.enit.fr/ontologies).
* archivo.csv: list of download URLs for the ontologies listed in [DBpedia Archivo](https://www.dbpedia.org/resources/archivo/)


