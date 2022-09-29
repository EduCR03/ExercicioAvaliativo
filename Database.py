import pymongo
from pymongo import MongoClient

from AulaDB import AulaDB


class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://EduCR03:root@cluster0.nxnlr5q.mongodb.net/test"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

        _aulaDB = AulaDB()

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

