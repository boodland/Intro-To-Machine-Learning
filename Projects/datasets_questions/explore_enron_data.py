
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
import re

def print_data_info(title, data):
    print(f'########## {title} ############\nSIZE: {len(data)} items')
    print(data)
    print()

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

enron_data_persons = [person for person in enron_data.keys()]
print_data_info('ENRON PERSONS', enron_data_persons)

enron_data_person_features = set(
    [feature for person in enron_data_persons for feature in enron_data[person].keys()]
)
print_data_info('ENRON PERSON''S FEATURES', enron_data_person_features)

enron_data_pois = [person for person in enron_data_persons if enron_data[person]["poi"]]
print_data_info('ENRON POIS', enron_data_pois)

with open("../final_project/poi_names.txt", 'r') as f:
    poi_names = [line for line in f.read().split("\n") if line.startswith('(')]

poi_names_processed = [re.sub(r'[(),]', '', poi_name).split(' ') for poi_name in poi_names]
poi_names_dictionary = {f'{surname.upper()} {name.upper()}': is_poi=='y' for is_poi, surname, name in poi_names_processed}
print_data_info('POI CANDIDATES', poi_names_dictionary)

enron_data_pois_in_poi_names = [enron_data_poi for poi_name in poi_names_dictionary.keys() for enron_data_poi in enron_data_pois if poi_name in enron_data_poi]
print_data_info('ENRON POIS IN POI CANDIDATES', enron_data_pois_in_poi_names)

print(f"James Prentice's total stock value = {enron_data['PRENTICE JAMES']['total_stock_value']}")
