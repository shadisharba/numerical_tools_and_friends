# https://medium.com/@inexturesolutions/data-serialization-in-python-json-vs-pickle-316bd5369f85

import pickle

data = '{"name": "John", "age": 30, "city": "New York"}'

pickle_data = pickle.dumps(data)  # serialize data to a binary string
print(pickle_data)

decoded_data = pickle.loads(pickle_data)  # deserialize data from a binary string
print(decoded_data)
