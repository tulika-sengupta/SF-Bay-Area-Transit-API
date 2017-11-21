import requests
from lxml import etree as et
import timeit

agency = ""

def getAgencyName(root, agencyName):
    for child in root.findall(".//{http://www.netex.org.uk/netex}SiriOperatorRef"):
        if child.text == agencyName:
            global agency
            agency = child.getparent().find('{http://www.netex.org.uk/netex}PrivateCode').text
            break


def validateAgencyName(agencyName):
    r = requests.get('https://api.511.org/transit/operators?api_key=520762a4-26b7-4e24-ac40-648eb29283a0&Format=xml')
    d = r.content
    root = et.fromstring(d)
    getAgencyName(root, agencyName)
    return agency