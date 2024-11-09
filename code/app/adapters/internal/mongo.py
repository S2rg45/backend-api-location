

import uuid
import pymongo



class MongoAdapter:
    def __init__(self, host, db_name, collection_name):
        self.host = host
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = pymongo.MongoClient(self.host)
        self.db = self.client[self.db_name]

    # --------------------------------------------------------------------------------
    # Method close_connection
    def close_connection(self):
        self.client.close()


    # get all data from the collection
    def get_collection_data(self):
        collection = self.db[self.collection_name]
        return collection.find({})
    

    # get specific data from the collection
    def get_specific_data(self, query):
        collection = self.db[self.collection_name]
        return collection.find_one(query)
    

    # specific data from the collection and update
    def get_data_and_update(self, query, update_query ):
        collection = self.db[self.collection_name]
        return collection.find_one_and_update(query, {"$set": update_query})
    

    #  insert data in the collection
    def insert_data_collection(self, data):
        insert_data = self.db[self.collection_name].insert_one(data)
        return insert_data