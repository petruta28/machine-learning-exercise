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


