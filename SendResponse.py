def sendResponseToSlack(time, s, stopCode, validStopCode, self):
    if validStopCode == False:
        self.response.write("Please enter valid stop code")
    else:
        if len(time) >= 1:
            self.response.write(s + " Buses arriving at bus stop " + stopCode + " at  " + str(time))

        else:
            self.response.write(s + " No buses arriving at bus stop " + stopCode)
