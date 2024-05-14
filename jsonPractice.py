#import the json library so that we can use the functions included
import json

#Create a dictionary with key, value pairs
data1 = {

  'name': 'John Doe',
  'age':30,
  'city': 'Tacoma, Wa',
  'interests':[
    'Hiking',
    'Running',
    'Bible',
    'Snowboarding',
    'Coding'
  ],
  'is_student': True

}

#Create a json file and writing the python object contents to the json file
with open('data1.json','w') as json_file:

  json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")

#Load and create a json file
with open('data1.json','r') as json_file:

  #Create an object called loaded_data. Load the json file into arguemnt parameter
  loaded_data = json.load(json_file)

print("Sucessfully able to read data1.json")
print(loaded_data)

#Altering the JSON object
loaded_data['age'] = 27
loaded_data['interests'].append('Secret Hobby')
#print(loaded_data['interests'][0])

#Rewrite the changes to the JSON file
with open('data1.json','w') as json_file:

  json.dump(loaded_data,json_file,indent=4)

print("Data has been updated and written to data1.json")