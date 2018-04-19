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
import csv


def remove_initials(name):
    parts = name.split(" ")
    for part in parts:
        if len(part) < 3:
            name = name.replace(part, "")
            print(name)
    return name.strip()


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print(len(enron_data))
# print(len(enron_data["SKILLING JEFFREY K"]))
# for key in enron_data:
#     print key, enron_data[key]
# print("James Prentice total stock value: ", enron_data["PRENTICE JAMES"]["total_stock_value"])
# print ("Nr of emails from Wesley Colwell to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["SKILLING JEFFREY K"]
salary_nan = 0
emails_nan = 0
total_payments = 0
total_payments_poi = 0
total_poi = 0
for name, features in enron_data.iteritems():
    print name, features
    if features['salary'] == 'NaN':
        salary_nan += 1
    if features['email_address'] == 'NaN':
        emails_nan += 1
    if features['total_payments'] == 'NaN':
        total_payments += 1
    if bool(features['total_payments'] == 'NaN') and bool(features['poi']):
        total_payments_poi += 1
    if features['poi']:
        total_poi += 1

print('Salaries not nan: ', len(enron_data) - salary_nan)
print('Emails not nan:', len(enron_data) - emails_nan)
print('Total payments nan: ', total_payments)
print ('Percentage: ', (100*total_payments)/len(enron_data))
print('Number of POIs that have total_payments = NaN and percentage of these among total POIs: ', total_payments_poi, (total_payments_poi*100)/total_poi)
print('Number of total people in the datatset is: ', len(enron_data) + 10)
print('Number of folks with NaN for total payments: ', total_payments + 10)
print("Total number of pois: ", total_poi + 10)
print("Total number of Pois with NaN total_payments: ", total_payments_poi + 10)