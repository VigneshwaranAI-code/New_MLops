
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
import certifi
import json
import sys

ca = certifi.where() #http connection  

mangodp = os.getenv("MONGO_DB_URL")

# uri = mangodp

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)/



import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exeption import NetworksecurityException
from networksecurity.logging.logger import logging 


class ETLpipeline:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 


    def cv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # data = data.T.to_json(orient='records', lines=True)
            recored = list(json.loads(data.T.to_json()).values())
            return recored

        except Exception as e:
            raise NetworksecurityException(e, sys)

    def insert_data_mongodb(self,records, database, collection):
        try:
            self.database =   database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(mangodp)
            
            self.db = self.mongo_client[self.database]
            self.collection = self.db[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworksecurityException(e, sys)

if __name__ == "__main__":
        etl = ETLpipeline()
        records = etl.cv_to_json("newwork_Data/phisingData.csv")
        record=etl.insert_data_mongodb(records, "vicky", "newwork_data")
        logging.info("Data inserted successfully")
        print(record)
        
    