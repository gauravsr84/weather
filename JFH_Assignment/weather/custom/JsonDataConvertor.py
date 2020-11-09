import json

class Weather:
    def __init__(self, temperature_value, temperature_unit):
        self.temperature_value = temperature_value
        self.temperature_unit = temperature_unit

    @staticmethod
    def get_json_dict(input_json):
        if(len(json_dict) > 0):
            json_dict = json.loads(input_json)
            return Weather(**json_dict)
