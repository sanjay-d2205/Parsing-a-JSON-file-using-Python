import json
#read file
json_fi= open('C:/Users/sanju/PycharmProjects/pythonProject/test.json','r') #file location
jsondata=json_fi.read()

#parse
# Convert string to Python dict
employee_dict = json.loads(jsondata)
for i in employee_dict['employee']:
    print('id:' +i['id'])
    print('department:' +i['department'])

    print('name:' +i['name'])

