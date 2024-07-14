import json

# Load configuration file of your selected model
with open("config.json") as json_file:
    config = json.load(json_file)


# Implement your classifier model class
class Classifier():
    def __init__(self, n_classes):
        pass

    def forward(self, input_ids, attention_mask):
        pass
