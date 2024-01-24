#!/usr/bin/env python3
""" Python script that lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """function to list all documents in a collection"""
    result = mongo_collection.find()
    return [doc for doc in result]
