import requests
import json


def findAgencyFromESDb(stopCode, self):
    q = 'stopCode:"' + stopCode + '"'
    response = requests.get('https://elasticsearch-rest.greenfieldlabs.io/transit-stops/_search?size=10000&q='+q)
    results = json.loads(response.text)

    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']))
        return (str(doc['_source']['agency']))
