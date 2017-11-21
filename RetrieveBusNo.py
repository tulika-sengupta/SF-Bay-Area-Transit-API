import requests
from lxml import etree as et

def retrieveBusNo(agency, datedVehicleJourneyRef, vehicleNo):
    r = requests.get(
        'http://api.511.org/transit/VehicleMonitoring?api_key=520762a4-26b7-4e24-ac40-648eb29283a0&Format=xml&agency=' + agency)
    d = r.content
    root = et.fromstring(d)

    for i,t in enumerate(datedVehicleJourneyRef):
        getBusNo(root, datedVehicleJourneyRef[i], vehicleNo)
    return vehicleNo

def getBusNo(root, datedVehicleJourneyRef, vehicleNo):
    for child in root.findall(".//DatedVehicleJourneyRef"):
        if child.text == datedVehicleJourneyRef:
            c = child.getparent().getparent().find('VehicleRef')
            vehicleNo.append(c.text)
            break;
