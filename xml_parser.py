import xml.etree.ElementTree as ET

from pprint import pprint

import json


def parser(tag):
    data = {}
    if len(tag) == 0:
        return tag.text.strip()
    else:
        for child in tag:
            if child.tag not in data:
                data[child.tag] = [parser(child)]
            else:
                data[child.tag].append(parser(child))
        return data


def write_to_file(file_name: str, data: dict):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


def main(file_path=None):
    if file_path is None:
        file_path = 'data/29-22-0-505-01-292_5c7ca0bc-4fad-20e3-55af-42e6ae387be8.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = parser(root)

    write_to_file('some_data', data)
