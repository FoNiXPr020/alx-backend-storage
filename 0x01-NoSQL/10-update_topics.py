#!/usr/bin/env python3
"""
function documentation
"""


def update_topics(mongo_collection, name, topics):
    """
    function documentation
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
