#!/usr/bin/env python3

# Function to create a dictionary from two lists: one for keys and one for values
def create_dictionary(keys, values):
    return dict(zip(keys, values))

# Function to find shared values between two dictionaries
def shared_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())

if __name__ == "__main__":
    # Example test runs for create_dictionary and shared_values
    keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    
    print("Create Dictionary:", create_dictionary(keys, values))  # Test for create_dictionary

    dict1 = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
    dict2 = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
    
    print("Shared Values:", shared_values(dict1, dict2))  # Test for shared_values
