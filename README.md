# SF-Bay-Area-Transit-API

PROGRAMMING LANGUAGE:
Python 3.0

REQUIREMENTS:
1)	Localtunnel
2)	Used Rest API to query Elastic Search in Python.

SLACK CONFIGURATION:
1)	In order to establish communication between my local computer and slack, I have used “localtunnel”. The localtunnel will provide me with a temporary domain name. 
2)	Now go to the “Edit Configuration” page of Slash Comands, and enter the above mentioned URL followed by the slash command “/slack511” in the URL parameter. 
3)	This will help Slack in communicating with my local PC.

HOW TO RUN THE PROJECT:
1)	Open project Slack511.
2)	Run “main.py”
3)	Now run the “localtunnel” and obtain the temporary URL.
4)	Go to Slack.com -> Slash Commands -> Custom Integration Settings. 
•	Enter the command “/slack511” in the ‘Command’ parameter.
•	Enter the URL obtained using localtunnel followed by “/slack511” in the URL parameter. It will look something like this -  “https://wewnmqsujp.localtunnel.me/slack511”
5)	Save the changes.
6)	Now run the command- /slack511.

FLOW OF THE SYSTEM:
1)	Slack Channel receives user request in the form of – “/slack511 stopCode”
2)	Slack uses the URL parameter to communicate with the backend processing.
3)	On receiving the slack request, Elastic Search database is hit with the ‘stopCode’ value, to retrieve the agency name.
4)	The retrieved agency name is then sent to the API: Operator to find the correct agency code.
5)	On receiving the correct agency code, Real-time predictions at a Stop API is hit with the agency code and the stopCode value to fetch the arrival time and ‘DatedJourneyVehicleRef’ of the buses.
6)	The DatedJourneyVehicleRef is then used to find the bus number by sending request to the Real-time Vehicle Monitoring API. 
7)	The arrival obtained at step (6), is then sent to a TimeConverter function which converts the time into 12 hour format.
8)	The final result is then sent back to the slack channel.

DEMO:
The demo of the project can be found at this Youtube URL: 
https://youtu.be/REWfUd9vk48
