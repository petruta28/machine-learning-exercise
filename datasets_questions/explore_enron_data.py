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
print(len(enron_data))
print(len(enron_data["SKILLING JEFFREY K"]))
for key in enron_data:
    print key, enron_data[key]["poi"]

new_dict = {}
for key in enron_data:
    if enron_data[key]["poi"]:
        new_dict[remove_initials(key)] = enron_data[key]

print(len(new_dict.keys()))
# print(names)

with open("../final_project/poi_names.csv", "r") as infile:
    reader1 = csv.reader(infile)

    summ1 = sum(1 for row in reader1 if ((row[0][3:] + row[1]).strip().upper() in new_dict))
    # for row in reader1:
    #     print((row[0][3:] + row[1]).strip())
print(summ1)





