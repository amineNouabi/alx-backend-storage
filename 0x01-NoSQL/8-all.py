#!/usr/bin/env python3
"""
This module contains the function all.

"""

from pymongo.collection import Collection, Cursor


def list_all(mongo_collection: Collection) -> Cursor:
    """
    list all documents in a collection
    """
    return mongo_collection.find()
