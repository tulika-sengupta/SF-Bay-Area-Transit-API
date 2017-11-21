from ElasticSearchClass import findAgencyFromESDb
from RetrieveValidAgencyName import validateAgencyName
from RetrieveArrivalTime import retrieveTime
from RetrieveBusNo import retrieveBusNo
from TimeConverter import formatTime
from SendResponse import sendResponseToSlack

def findAgency(stopCode, self):
    timeList = []
    busNum = []

    #Retrieve Agency Name from Elastic Search DB
    agency = findAgencyFromESDb(stopCode, self)

    if agency is not None:

        #Validate the Agency Name From The Transit API: Operator
        validAgencyName = validateAgencyName(agency)

        #Retrieve the Bus Timings and Vehilcle Journey Reference From API: Real-time predictions at a Stop
        time, vehicleJourneyRef = retrieveTime(str(validAgencyName), str(stopCode), timeList)
        time = formatTime(time)

        #Retrieve the BUS number using the vehicleJourneyRef From API: Real-time Vehicle Monitoring
        # bus = retrieveBusNo(str(validAgencyName), vehicleJourneyRef, busNum)

        s = agency + "(" + validAgencyName + ")"
        sendResponseToSlack(time, s, stopCode, True, self)

    else:
        sendResponseToSlack([], '', '', False, self)