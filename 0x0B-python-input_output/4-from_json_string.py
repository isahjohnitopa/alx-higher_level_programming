#!/usr/bin/python3
"""Defines a function that returns an object rep. of a    JSON string"""
import json


def from_json_string(my_str):
    """Returns the object rep of the JSON string."""
    return json.loads(my_str)
