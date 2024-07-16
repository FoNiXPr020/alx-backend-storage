#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def get_stats(collection):
    """Returns stats about the collection"""
    all_logs = collection.count_documents({})
    method_counts = {
        "GET": collection.count_documents({"method": "GET"}),
        "POST": collection.count_documents({"method": "POST"}),
        "PUT": collection.count_documents({"method": "PUT"}),
        "PATCH": collection.count_documents({"method": "PATCH"}),
        "DELETE": collection.count_documents({"method": "DELETE"})
    }
    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    return all_logs, method_counts, status_check


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    all_logs, method_counts, status_check = get_stats(collection)
    print("{} logs\n Methods:\n {}"
          .format(all_logs, "\n\t".join(
              "  method {}: {}".format(method, count)
              for method, count in method_counts.items())))
print("{} status check".format(status_check))
