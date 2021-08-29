import requests
import json


def wikidata_pull(sql_query, output_file='results/wikidata-query.json'):
    """Performs a query on the Wikidata Query Service and saves the output to a file.
    Keyword arguments:

    :query: SQL query
        (str)
    :output_file: directory and name of the desired output file
        (str: default: results/wikidata-query.json)

    """
    url = 'https://query.wikidata.org/sparql'
    r = requests.get(url, params={'format': 'json', 'query': sql_query})
    r.raise_for_status()
    data = r.json()
    with open(output_file, 'w+') as file:
        json.dump(data, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    query = '''
    SELECT ?date ?event ?eventLabel 
    WHERE
     {
         # find events
        ?event wdt:P31/wdt:P279* wd:Q1190554.
        # with a point in time or start date
        OPTIONAL { ?event wdt:P585 ?date. }
        OPTIONAL { ?event wdt:P580 ?date. }
        # but at least one of those
        FILTER(BOUND(?date) && DATATYPE(?date) = xsd:dateTime).
        # not in the future, and not more than 31 days ago
        BIND(NOW() - ?date AS ?distance).
        FILTER(0 <= ?distance && ?distance < 31).
        # and get a label as well
        OPTIONAL {
            ?event rdfs:label ?eventLabel.
            FILTER(LANG(?eventLabel) = "en").
        }
     }
    # limit to 10 results so we don't timeout
     LIMIT 5
    '''

    wikidata_pull(query)
