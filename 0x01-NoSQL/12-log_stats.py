#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def get_stats(collection):
    """Returns stats about the collection"""

    print('{} logs'.format(collection.count_documents({})))
    print('Methods:')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks = len(list(
        collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks))


if __name__ == "__main__":
    """Prints stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    get_stats(client.logs.nginx)
