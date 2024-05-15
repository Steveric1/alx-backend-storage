#!/usr/bin/env python3

"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_nginx_start():
    """
    stats about Nginx logs stored in MongoDB
      Database - logs
      Collection - nginx

    Objective:
      Provide some stat stored in MongoDB
    Execution
      - connect to the MongoDB
      - create nginx collection
      - get the total number of document in the collection
      - get the number of documents with the method ["GET", "POST", "PUT", "PATCH", "DELETE"]
      - get the number of documents with the path /status
    """

    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    total_log = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # count logs with path /status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # display the result
    print(f"{total_log} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_count} status check")


if __name__ == "__main__":
    get_nginx_start()
