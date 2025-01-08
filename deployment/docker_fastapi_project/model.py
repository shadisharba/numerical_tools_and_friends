### use the previous lib in the predict function
import json
from classifier import Classifier

# Load configuration file of your selected model
with open("config.json") as json_file:
    config = json.load(json_file)


# Implement your selected model class
class Model:
    def __init__(self):
        pass

    def predict(self, text):
        pass


# Create an object for your implemented class       
model = Model()


# Use the function to call your model.
def get_model():
    return model
