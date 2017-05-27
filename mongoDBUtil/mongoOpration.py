#!/bin/python
# -*- coding: utf-8 -*-

from pymongo import *
from pymongo.errors import BulkWriteError


def getMongoConnection(db_name, collection_name, host='localhost'):
    client = MongoClient(host, 27017)
    db = client[db_name]
    collection_useraction = db[collection_name]
    return collection_useraction


def autoIncrement():
    ids = getMongoConnection("videos", "ids")
    res = ids.find_one()
    return res["_id"]

def bulkInsertDocument():
    collection = getMongoConnection("videos", "testVideo")
    bulk = collection.initialize_ordered_bulk_op()
    # collection.insert_one({'_id':autoIncrement()},{"$inc":{"_id":1}})
    # print "success insert "
    for count in range(0,100):
        bulk.insert({'_id': count})
    try:
        result = bulk.execute()
        print result
    except BulkWriteError as bwe:
        print bwe.details

bulkInsertDocument()