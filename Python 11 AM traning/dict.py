# #Defining dictionary
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# print(dict)
# print("The length of the dictionary 'dict' is:", len(dict))
# print("The above dict is of type:", type(dict))
# print("The address of the Dictionary 'dict' is:", id(dict))

# #Retrieving values from a dictionary
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# print(dict['Name'])
# print(dict['Age'])
# print(dict['City'])

# #Operations on Dictionaries
# #Modify the dictionary
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# dict['City'] = 'Bengaluru'
# print(dict)         #city is updated to 'Bengaluru'

# #Adding new key:value pair into dictionary
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# dict['Mobile'] = 9618114253
# print(dict)         #New key:value pair is added in the dictionary.

# #deleting key:value pair from dictionary
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# del dict['Age']
# print(dict)

# #Membership operators
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# print('Name' in dict)       #True
# print('Mobile' not in dict) #True

# #Dictionary Methods
# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# dict.clear()
# print(dict)     #Returns empty dictionary after clearing all the key:value pairs.

# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# d1 = dict.copy()
# print("The newly copied dictionary d1 is:", d1)

# d = ('key1','key2','key3')
# v = (10,20,30)
# d1 = dict.fromkeys(d,v) #Output => {'key1': (10, 20, 30), 'key2': (10, 20, 30), 'key3': (10, 20, 30)}
# print(d1)

# dict = {'Name':'Aditya','Age':35,'City':'Hyderabad'}
# print(dict.get('Name'))

#Program to retrieve keys, values and key:value pairs from a dictionary
# d = {'Name':'Aditya','Age':35,'City':'Hyderabad'}

# print(d.keys()) # Output => dict_keys(['Name', 'Age', 'City'])
# print(d.values()) # Output => dict_values(['Aditya', 35, 'Hyderabad'])
# print(d.items()) # Output => dict_items([('Name', 'Aditya'), ('Age', 35), ('City', 'Hyderabad')])

#Program to enter key:values through user input and calculate the sum.
# d1 = eval(input("Enter the dictionary : "))
# print(d1)
# print(type(d1))
# sum1 = sum(d1.values())
# print(sum1)

#initializing an empty dictionary
my_dict = {}

# Get the number of key-value pairs to add
n = int(input("How many items do you want to add to the dictionary? "))

# Loop to take key-value inputs
for _ in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    my_dict[key] = value  # Add the key-value pair to the dictionary
print(my_dict)

s = sum(my_dict.values())
print(s)
