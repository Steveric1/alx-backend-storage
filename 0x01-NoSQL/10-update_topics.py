#!/usr/bin/env python3

"""Python function that changes all topics of a school document based on the name:"""

from pymongo import MongoClient
from typing import List


def update_topics(mongo_collection: MongoClient,
                  name: str, topics: List[str]) -> str:
    """Update topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
