def formatTime(time):
    for i, t in enumerate(time):
        strippedTime = t[t.find("T") + 1:t.find("Z")]
        timeSegments = strippedTime.split(':')
        hour = timeSegments[0]
        min = timeSegments[1]
        sec = timeSegments[2]

        suffix = "PM" if int(hour) >= 12  else "AM"
        hour = (int(hour) + 11) % 12 + 1
        formattedTime = str(hour) + ":" + str(min) + ":" + str(sec) + "" + suffix
        time[i] = formattedTime
    return time