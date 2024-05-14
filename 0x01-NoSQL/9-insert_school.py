#!/usr/bin/env python3

"""Python function that inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection: MongoClient, **kwargs) -> str:
    """Python function that inserts a new document in a collection based on kwargs"""
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
