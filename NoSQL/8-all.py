#!/usr/bin/env python3
"""Module to learn about using MongoDB with Python"""


def list_all(mongo_collection):
    """lists all documents in a collection""" 
    return list(mongo_collection.find())
