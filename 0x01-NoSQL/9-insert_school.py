#!/usr/bin/env python3
"""python script that insert new document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """python function to insert..."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
