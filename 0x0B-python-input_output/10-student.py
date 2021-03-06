#!/usr/bin/python3
""" class Student that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes arguments
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dict of class
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict
