#!/usr/bin/env python3
""" Python script  that returns the list of
school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """function ..."""
    tf = {'topics': {'$elemMatch': {'$eq': topic}}}
    return [doc for doc in mongo_collection.find(tf)]
