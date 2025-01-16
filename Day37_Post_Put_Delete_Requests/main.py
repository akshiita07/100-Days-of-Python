# Requests:
# 1. get: ask an external system to retrieve a particular piece of data & we get response
# 2. post: we give external system some data & are not interested in response (only if successful/not)
# 3. put: update a piece of data in external service
# 4. delete: delete a piece of data in external service

import requests
# post our habit on pixela to be tracked: https://pixe.la/
parameters={
    "token":"any1random2api3key4generated5",
    "username":"akshitapathak07",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# 1. REGISTERING USER:
# response=requests.post(url="https://pixe.la/v1/users",json=parameters)  #here parameters are provided as JSON!! (not params as in GET)
# print(response)
# print(response.text)    #https://pixe.la/@akshitapathak07

parameters2={
    "id":"graph1",
    "name":"100 Days of Python",
    "unit":"hours   ",      #min/hours/km
    "type":"int",        #int/float
    "color":"sora", #from documentation corresponding to blue
}

headers={
    "X-USER-TOKEN":"any1random2api3key4generated5",      #authentication header
}

# 2. GETTING GRAPH:
# response=requests.post(url="https://pixe.la/v1/users/akshitapathak07/graphs",json=parameters2,headers=headers)
# print(response.text)      #https://pixe.la/v1/users/akshitapathak07/graphs/graph1
# https://pixe.la/v1/users/akshitapathak07/graphs/graph1.html


from datetime import datetime
today=datetime.now()

# year=today.year
# month=today.month
# if month<10:
#     month=f"0{month}"
# date=today.day
# if date<10:
#     date=f"0{date}"
# full_date=f"{year}{month}{date}"
# print(full_date)

# STRFTIME MODULE
full_date=today.strftime("%Y%m%d")
# print(full_date)

parameters3={
    "date":full_date,      #yyyyMMdd: 20250117
    "quantity":str(input("Did you complete a day today? Yes:1")),         #coded today
}
# 3. POSTING PIXEL:
response=requests.post(url="https://pixe.la/v1/users/akshitapathak07/graphs/graph1",json=parameters3,headers=headers)
print(response.text) 


parameters4={
    "quantity":"10",         #update: coded 10 today
}
# 4. PUT TO UPDATE A GIVEN PIXEL
# response=requests.put(url=f"https://pixe.la/v1/users/akshitapathak07/graphs/graph1/{full_date}",json=parameters4,headers=headers)
# print(response.text) 

# 5. DELETE TO remove A GIVEN PIXEL
# response=requests.delete(url=f"https://pixe.la/v1/users/akshitapathak07/graphs/graph1/{full_date}",headers=headers)
# print(response.text) 