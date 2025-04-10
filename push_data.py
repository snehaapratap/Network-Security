import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data=data.reset_index(drop=True,inplace=True)
            records=list(data.T.to_dict().values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    file_path="networkdata\phishingData.csv"
    DATABASE="snehapratap248"
    Collection="networkdata"
    networkjobj=NetworkExtract()
    records=networkjobj.cv_to_json_convertor(file_path=file_path)
    no_of_records=networkjobj.insert_data_mongodb(records=records,database=DATABASE,collection=Collection) 
    print(no_of_records) 