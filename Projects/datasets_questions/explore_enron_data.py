
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
    print()
    print(f'########## {title} ############\nSIZE: {len(data)} items')
    print(data)

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

enron_data_people = [person for person in enron_data.keys()]
print_data_info('ENRON PEOPLE', enron_data_people)

enron_data_person_features = set(
    [feature for person in enron_data_people for feature in enron_data[person].keys()]
)
print_data_info('ENRON PERSON''S FEATURES', enron_data_person_features)

enron_data_pois = [person for person in enron_data_people if enron_data[person]["poi"]]
print_data_info('ENRON POIS', enron_data_pois)

with open("../final_project/poi_names.txt", 'r') as f:
    poi_names = [line for line in f.read().split("\n") if line.startswith('(')]

poi_names_processed = [re.sub(r'[(),]', '', poi_name).split(' ') for poi_name in poi_names]
poi_names_dictionary = {f'{surname.upper()} {name.upper()}': is_poi=='y' for is_poi, surname, name in poi_names_processed}
print_data_info('POI CANDIDATES', poi_names_dictionary)

enron_data_pois_in_poi_names = [enron_data_poi for poi_name in poi_names_dictionary.keys() for enron_data_poi in enron_data_pois if poi_name in enron_data_poi]
print_data_info('ENRON POIS IN POI CANDIDATES', enron_data_pois_in_poi_names)

print(f"James Prentice's total stock value = {enron_data['PRENTICE JAMES']['total_stock_value']}")

print(f"Wesley Colwell's email messages to poi = {enron_data['COLWELL WESLEY']['from_this_person_to_poi']}")

print(f"Jeffrey K Skilling's value of stock options exercised = {enron_data['SKILLING JEFFREY K']['exercised_stock_options']}")

print(f"Kenneth L Lay's total payments = {enron_data['LAY KENNETH L']['total_payments']}")
print(f"Jeffrey K Skilling's total payments = {enron_data['SKILLING JEFFREY K']['total_payments']}")
print(f"Andrew S Fastow's total payments = {enron_data['FASTOW ANDREW S']['total_payments']}")

enron_data_people_with_quantified_salary = {person: enron_data[person]['salary'] for person in enron_data_people if enron_data[person]['salary'] != 'NaN'}
print_data_info('ENRON PEOPLE WITH QUANTIFIED SALARY', enron_data_people_with_quantified_salary)

enron_data_people_with_email_address = {person: enron_data[person]['email_address'] for person in enron_data_people if enron_data[person]['email_address'] != 'NaN'}
print_data_info('ENRON PEOPLE WITH EMAIL ADDRESS', enron_data_people_with_email_address)

enron_data_people_without_quantified_salary= enron_data_people - enron_data_people_with_quantified_salary.keys()
print_data_info('ENRON PEOPLE WITHOUT QUANTIFIED SALARY', enron_data_people_without_quantified_salary)
print(f"% OF TOTAL: {len(enron_data_people_without_quantified_salary)/len(enron_data_people)}")

enron_data_pois_without_total_payments = [person for person in enron_data_pois if enron_data[person]['total_payments'] == 'NaN']
print_data_info('ENRON POIs WITHOUT TOTAL SALARY', enron_data_pois_without_total_payments)
print(f"% OF TOTAL POIs: {len(enron_data_pois_without_total_payments)/len(enron_data_pois)}")
