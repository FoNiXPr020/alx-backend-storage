#!/usr/bin/env python3
"""
function documentation
"""


def schools_by_topic(mongo_collection, topic):
    """
    function documentation
    """
    return mongo_collection.find({"topics": topic})
