# Created by: Gavin Zhou
# Created on: Dec 2017
# Created for: ICS3U


from enum import Enum

# 1. about street
street_type = Enum('Avenue', 'Boulevard', 'Crescent', 'Lane', 'Road')

# 2. about provinces
provinces = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')


class Address():
    def __init__(self, name, street_number, street_name, street_type, province, city, postal_code):
        self.name = name
        self.street_number = street_number
        self.street_name = street_name
        self.street_type = street_type
        self.province = province
        self.city = city
        self.postal_code = postal_code
        


user_name = raw_input("Enter your name: ")

user_street_number = raw_input("Enter your street number: ")

user_street_name = raw_input("Enter your street name: ")

print("Choose your street type: Street, Boulevard, Road, Avenue, Crescent")
user_street_type = raw_input("Enter your street type: ")
if user_street_type in street_type:
    print('Valid street type')

    print("Enter the abbreviation of the province in this list: AB (Alberta), BC (British Columbia), MB (Manitoba), NB (New Brunswick), NL (Newfoundland and Labrador), NT (Northwest Territories), NS (Nova Scotia), NU (Nunavut), ON (Ontario), PE (Prince Edward Island), QC (Quebec), SK (Saskatchewan)")
user_province= raw_input("Enter your province(abbreviation): ")
if user_province in provinces:
        print('Valid province')

user_city = raw_input("Enter your city: ")

user_postal_code = raw_input("Enter your postal code: ")


user_input = Address(user_name, user_street_number, user_street_name, user_street_type, user_city, user_province, user_postal_code)
print(user_input.name + '\n' + user_input.street_number + ' ' + user_input.street_name + ' ' +  user_input.street_type + '\n' +  ' ' + user_input.province + ' ' + user_input.city + ' ' + user_input.postal_code)



