#!/usr/bin/env python3
"""

This module contains the function all.

"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    return mongo_collection.find()
