import json
import os

DATA_PATH="data/"

def get_json_input_files(path_to_json=DATA_PATH) -> dict:
    json_input = {}
    for file_name in [file for file in os.listdir(path_to_json) if file.endswith('input.json')]:
        with open(path_to_json + file_name) as json_file:
            data = json.load(json_file)
            json_input[file_name] = data
    return json_input


def get_json_output_files(path_to_json=DATA_PATH) -> dict:
    json_input = {}
    for file_name in [file for file in os.listdir(path_to_json) if file.endswith('output.json')]:
        with open(path_to_json + file_name) as json_file:
            data = json.load(json_file)
            json_input[file_name] = data
    return json_input