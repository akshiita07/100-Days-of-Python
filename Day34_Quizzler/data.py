import requests

# add arameters here:
parameters={
    "amount":20,  
    "type":"boolean",    
    "category":18,
}
response=requests.get(url="https://opentdb.com/api.php",params=parameters)
question_data=response.json()["results"]
# print(question_data)