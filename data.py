import json

DATA_BASE_FILE = "data_base.json"


def add_entry(name, phone):
    try:
        data = read_data(DATA_BASE_FILE)
        data[name] = phone
        save_data(data, DATA_BASE_FILE)
        return True
    except:
        return False


def find(name):
    data = read_data(DATA_BASE_FILE)
    return data[name]


def read_data(file_name):
    with open(file_name, encoding="utf-8") as data_base:
        return json.load(data_base)


def save_data(data, file_name):
    with open(file_name, "w", encoding="utf-8") as data_base:
        json.dump(data, data_base)


def import_data(file_name):
    current_data = read_data(DATA_BASE_FILE)
    new_data = read_data(file_name)
    merged_data = {**current_data, **new_data}
    save_data(merged_data, DATA_BASE_FILE)


def export_data(file_name):
    data = read_data(DATA_BASE_FILE)
    save_data(data, file_name)