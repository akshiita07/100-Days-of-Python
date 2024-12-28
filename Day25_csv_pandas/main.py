#open csv file:

# Method1: using files
'''
with open("./Day25_csv_pandas/weather_data.csv") as data_files:
    data=data_files.readlines()
    print(data)
'''

# Method2: using inbuilt library: 
'''
import csv
with open("./Day25_csv_pandas/weather_data.csv") as data_files:
    data=csv.reader(data_files)
    # print(data) returns an object that can be looped thru
    temperature=[]
    for row in data:
        print(row)
        if row[1]!='temp':
            temperature.append(int(row[1]))     #as integer
    
    print("List of temperatures: ")
    print(temperature)
'''
    
# Method3: using inbuilt library: 
import pandas
data=pandas.read_csv("./Day25_csv_pandas/weather_data.csv")
print(data)
print("List of temperatures: ")
print(data["temp"])
print("Types of data: ")
print(type(data))       #pandas dataframe object