#!/usr/bin/python3
"""
This module contains a class called Base
"""
import json
import csv


class Base:
    """
    This is the Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f'{cls.__name__}.json'
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        json_str = Base.to_json_string(list_dicts)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new_instance = cls(**dictionary)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = f'{cls.__name__}.json'

        try:
            with open(filename, encoding="utf-8") as f:
                json_list = f.read()
        except FileNotFoundError:
            return []
        list_dicts = Base.from_json_string(json_list)
        list_instances = []

        for dict in list_dicts:
            list_instances.append(cls.create(**dict))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        # pegar a lista
        # para cada item, pegar os dicts
        # armazenar numa lista de dicts
        # percorer cada dict e armazenar na SyntaxWarning
        # Escrever a string no file
        filename = f'{cls.__name__}.csv'
        header = []
        if cls.__name__ == 'Rectangle':
            header = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            header = ['id', 'size', 'x', 'y']

        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        data = []

        for d in list_dicts:
            data.append(list(d.values()))

        with open(filename, 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        filename = f'{cls.__name__}.csv'
        header = []
        data = []
        with open(filename, encoding='utf-8') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            for row in csvreader:
                data.append(row)

        list_dicts = []
        for d in data:
            new_d = dict(zip(header, list(int(n) for n in d)))
            list_dicts.append(new_d)

        list_instances = []

        for d in list_dicts:
            list_instances.append(cls.create(**d))

        return list_instances
