#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
poi_names = open("../final_project/poi_names.txt", "r")
print('poi_names', poi_names.readline())

poi_person_count = 0
for line in poi_names:
    if (line.find('(y)') >= 0):
        poi_person_count += 1
        print('line', line)
print('poi_person_count', poi_person_count)


#print('enron_data', enron_data)
poi_count = 0
for key, value in enron_data.items():
    #print('key', key)
    if (value["poi"] == 1):
        poi_count += 1
print('poi_count', poi_count)

print(len(enron_data))

print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])

poi_list = []
for key, value in enron_data.items():
    if (key == "SKILLING JEFFREY K" or key == "LAY KENNETH L" or key == "FASTOW ANDREW S"):
        poi_list.append({key: value["total_payments"]})
        print(value["total_payments"])
print('poi_list', poi_list)

top_earner = None
current_value = 0
for item in poi_list:
    for key, value in item.items():
        if (current_value > value):
            pass
        else:
            current_value = value
            top_earner = item
print('top_earner', top_earner)

#print(enron_data)
non_nan_salary_count = 0
non_nan_email_count = 0

for key, value in enron_data.items():
    if (value["salary"] != 'NaN'):
        non_nan_salary_count += 1
    if (value["email_address"] != 'NaN'):
        non_nan_email_count += 1
print('non_nan_salary_count', non_nan_salary_count)
print('non_nan_email_count', non_nan_email_count)



nan_total_payments_count = 0
total_items = 0

for key, value in enron_data.items():
    total_items += 1
    if (value["total_payments"] == 'NaN'):
        nan_total_payments_count += 1
print('nan_total_payments_count', nan_total_payments_count)
print('total_items', total_items)
print((nan_total_payments_count / total_items) * 100)

total_poi_nan_total_payments_count = 0
for key, value in enron_data.items():
    if (value["total_payments"] == 'NaN' and value["poi"] == True):
        total_poi_nan_total_payments_count += 1
print('total_poi_nan_total_payments_count', total_poi_nan_total_payments_count)