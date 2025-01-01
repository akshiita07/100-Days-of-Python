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
'''
print(data)
print("List of temperatures: ")
print(data["temp"])
print("Types of data: ")
print(type(data))       #pandas dataframe object
print(type(data["temp"]))       #pandas series object

# convert pandas dataframe to dictionary
data_dict=data.to_dict()
print(data_dict)

# convert pandas series to list
data_list=data["temp"].to_list()
print(data_list)
print(len(data_list))
print(f"Average of temp is: {sum(data_list)/len(data_list)}")
print(f"Average of temp is: {data["temp"].mean()}")
print(f"Max value from temp is: {data["temp"].max()}")

conditions=data["condition"]        #match name of colm exactly
print(conditions)
conditions_method2=data.condition
print(conditions_method2)

'''

# GETTING DATA IN ROWS: 
print(data[data["day"]=="Monday"])
# print row of data that had max temp:
print(data[data["temp"]==data["temp"].max()])

monday_data=data[data.day=="Monday"]
print(monday_data.temp)
monday_data_temp=monday_data.temp[0]        #to get series object to integer
print(f"Temp in farenheit: {monday_data_temp*9/5+32}")
print(monday_data.condition)

# TO CREATE A DATA FRAME FROM SCRATCH:
my_dict={
    "subject":['np','convo','cao'],
    "scores":[94.1,84.44,68]
}
# create datafram from dictionary:
new_data=pandas.DataFrame(my_dict)
print(new_data)
# convert dataframe to csv file:
new_data.to_csv("new_data.csv")      #creates a new csv file