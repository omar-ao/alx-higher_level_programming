#!/usr/bin/python3
"""This is the ``11-student`` module
It defines one class Student
"""


class Student:
    """A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the instance

        Args:
            first_name: Student first name
            last_name: Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrivies a dictionary representation of
        Studnet instance

        Only attribute names contained in this list is
        retrieved. Otherwise all attributes are retrieved

        Args:
            attrs: A list of strings
        """
        obj_dict = self.__dict__
        if attrs is not None:
            return {attr: obj_dict[attr] for attr in attrs if attr in obj_dict}
        return obj_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json: A dictionary
        """
        for key in json:
            setattr(self, key, json[key])
