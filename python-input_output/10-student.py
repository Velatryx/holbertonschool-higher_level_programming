#!/usr/bin/python3
"""Defines a Student class with attribute filtering."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, return only the matching attributes.
        Otherwise, return all attributes.
        """
        if type(attrs) == list and all(type(item) == str for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__.copy()
