import requests
from lxml import etree as et
from TimeConverter import formatTime

vehicleJourneyRef = []
t = []

def retrieveTime(agency, stopCode, timeList):

    r = requests.get(
        'http://api.511.org/transit/StopMonitoring?api_key=520762a4-26b7-4e24-ac40-648eb29283a0&Format=xml&agency=' + agency + '&stopCode=' +
            stopCode)
    d = r.content
    root = et.fromstring(d)
    getTime(root, stopCode, timeList)
    return timeList[:2], vehicleJourneyRef[:2]

def getTime(root, stopCode, timeList):
    for child in root.findall(".//MonitoringRef"):
        if child.text == stopCode:
            c = child.getparent().find('MonitoredVehicleJourney')
            child1 = c.find('MonitoredCall/AimedArrivalTime')
            child2 = c.find('FramedVehicleJourneyRef/DatedVehicleJourneyRef')
            timeList.append(child1.text)

            if child2 is not None:
                global vehicleJourneyRef
                vehicleJourneyRef.append(child2.text)
            else:
                vehicleJourneyRef.append('')








                    # def retrieveTime(agency, stopCode, timeList):
#
#     r = requests.get(
#         'http://api.511.org/transit/StopMonitoring?api_key=520762a4-26b7-4e24-ac40-648eb29283a0&Format=xml&agency=' + agency + '&stopCode=' +
#             stopCode)
#     d = r.content
#     root = et.fromstring(d)
#     getTime(root, stopCode, timeList)
#     #timeList = formatTime(timeList[:2])
#     return timeList[:2], vehicleJourneyRef[:2]
#
# def getTime(root, stopCode, timeList):
#     for child in root:
#         if child.text == stopCode:
#             child1 = child.getparent().find('MonitoredVehicleJourney/MonitoredCall/AimedArrivalTime')
#             child2 = child.getparent().find('MonitoredVehicleJourney/FramedVehicleJourneyRef/DatedVehicleJourneyRef')
#             #child3 = child.getparent().find('MonitoredVehicleJourney/MonitoredCall/StopPointName')
#             if child1 is not None:
#                 timeList.append(child1.text)
#                 global stopName
#                 #stopName.append(child3.text)
#             if child2 is not None:
#                 global vehicleJourneyRef
#                 vehicleJourneyRef.append(child2.text)
#
#         getTime(child, stopCode, timeList)

#retrieveTime('AC', '50866', t)