import json

data_repo = '../../data_repo/'

# parse a JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)  # returns a dictionary

print(data['name'])  # access a value by key

for key, value in data.items():  # loop through all key-value pairs
    print(key, value)  # print key and value

data['email'] = 'john@example.com'  # add a new key-value pair
data['age'] = 31  # modify a value
del data['city']  # remove a key-value pair

# write the modified JSON data to a file
with open(f'{data_repo}/data_modified.json', 'w') as f:
    json.dump(data, f)

# write the modified JSON data to a string
json_string = json.dumps(data)
print(json_string)
