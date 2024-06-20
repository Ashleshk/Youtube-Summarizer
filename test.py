import json
from datetime import datetime
json_data = '''[
   {"first_name":"Ranee","last_name":"Thowless","email":"rthowless9@ft.com","company":"Greenfelder, Goyette and Steuber","birthdate":"1996-06-22"}
]'''

contacts = json.loads(json_data)
print(f'record count: {len(contacts)}')

# STEP 1: Print a list of formatted names (last, first)
for rec in range(0,10):
    print(contacts[rec]['first_name'],",",contacts[rec]['last_name'])
    
# STEP 2: Print a sorted list of birthdates
def convert_string_date(str):
    return datetime.strptime(str,'yyyy-mm-dd')

for rec in range(0,1):
    birthdates=contacts[rec]['birthdate']
sorted_dates = sorted(birthdates, key=lambda x: convert_string_date(x) if isinstance(x,str) else x)


for rec in range(0,1):
    print(sorted_dates)
