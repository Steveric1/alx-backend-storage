#!/usr/bin/env python3

"""Python function that returns the list of school having a specific topic"""

from pymongo import MongoClient
from typing import List


def schools_by_topic(mongo_collection: MongoClient, topic: List[str]) -> List[str]:
    """Returns the list of school having a specific topic"""
    topic = mongo_collection.find({"topics": topic})
    return topic
