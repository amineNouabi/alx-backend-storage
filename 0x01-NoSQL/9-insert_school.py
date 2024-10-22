#!/usr/bin/env python3
"""
This module contains the function insert_school.

"""

from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    insert a document in a collection based on kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
