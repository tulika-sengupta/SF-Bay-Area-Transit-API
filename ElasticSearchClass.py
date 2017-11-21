import requests
import json


def findAgencyFromESDb(stopCode, self):
    #scroll api: '10.40.163.67:9200/sn_index_data/sn-node2/_search?scroll=10m'
    q = 'stopCode:"' + stopCode + '"'
    response = requests.get('https://elasticsearch-rest.greenfieldlabs.io/transit-stops/_search?size=10000&q='+q)
    results = json.loads(response.text)

    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']))
        return (str(doc['_source']['agency']))

# def findAgencyFromESDb(stopCode, self):
#     #scroll api: '10.40.163.67:9200/sn_index_data/sn-node2/_search?scroll=10m'
#     q = 'stopCode:"' + stopCode + '"'
#     response = requests.get('https://elasticsearch-rest.greenfieldlabs.io/transit-stops/_search?size=10000&scroll=1m&q='+q)
#     # response = requests.get(
#     #     'https://elasticsearch-rest.greenfieldlabs.io/transit-stops/_search?size=10000&scroll=1m')
#     results = json.loads(response.text)
#
#     scrollid = results['_scroll_id']
#     scroll_size = results['hits']['total']
#     print ("Initial scroll id: " , scrollid)
#
#     i =0
#     while (scroll_size > 0):
#         print i
#         i = i+1
#         data = [doc for doc in results['hits']['hits']]
#         print ("Num of docs: " + str(len(results['hits']['hits'])))
#         for doc in data:
#             print("%s) %s" % (doc['_id'], doc['_source']))
#             #return (str(doc['_source']['agency']))
#         response = requests.get(
#             'https://elasticsearch-rest.greenfieldlabs.io/transit-stops/_search?scroll=2m&scroll_id='+scrollid)
#         results = json.loads(response.text)
#         scrollid = results['_scroll_id']
#         print ("Final scroll id: ", scrollid)
#         scroll_size = len(results['hits']['hits'])
#findAgencyFromESDb('55119', '')