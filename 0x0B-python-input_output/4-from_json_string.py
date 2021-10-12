#!/usr/bin/
""" function that returns an object (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Decodes to json
    :param my_obj: Parsed obj
    """
    return json.loads(my_str)
