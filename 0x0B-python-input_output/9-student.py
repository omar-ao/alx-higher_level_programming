#!/usr/bin/python3
"""This is the ``9-student`` module
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

    def to_json(self):
        """Retrives a dictionary representation of
        Studnet instance
        """
        return self.__dict__
