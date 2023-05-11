## Queries used to extract the numbers.
The data (`metadata_results.ttl` file) was loaded in a local Fuseki triplestore.

### Number of ontologies
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
select (count (distinct ?o) as ?count)
WHERE {
 ?o a owl:Ontology
}
```
Answer: 1961

### Number of concept schemes:
```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
select (count (distinct ?o) as ?count)
WHERE {
 ?o a skos:ConceptScheme
}
```
Answer: 587

### List all properties used:
```
select distinct ?prop
WHERE {
 ?onto ?prop ?d
}
```
### Give me the support of each property per ontology or concept scheme: 
```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
select ?prop (count (distinct ?onto) as ?support_ontology) (count (distinct ?concept) as ?support_concept_scheme)
WHERE {
  {
 ?onto ?prop ?d;
       a owl:Ontology
  }union
  {
    ?concept ?prop ?d1;
        a skos:ConceptScheme
  }
}group by ?prop
order by desc (?support_ontology)
```
Result: See `support_by_ontology_concept_scheme.csv`. If you remove the union and leave only one count, you will get the joined results `support_by_resource.csv` file.
