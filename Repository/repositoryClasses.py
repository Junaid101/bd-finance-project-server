from pymongo import MongoClient
import bson
import dotenv
import os
import datetime

loadEnvironment()

def newGUID():
    import uuid
    return str(uuid.uuid4())

def currentUTCDate():
    return datetime.datetime.utcnow()

def loadEnvironment():
    dotenv.load_dotenv()

def getConnectionString():
    return os.getenv("MONGO_CONN_STRING")

def getDefaultTenant():
    return os.getenv("DEFAULT_TENANT")

def getDefaultCollection():
    return os.getenv("DEFAULT_COLLECTION")

class RepositoryCollection():
    def __init__(self, collectionName = getDefaultCollection()):
        myClient = MongoClient(host = getConnectionString())
        self.database = myClient[getDefaultTenant()]
        self.activeCollection = self.database[collectionName]
        
    def insertOne(self, entityObject):
        assert isinstance(entityObject, BaseEntity)
        self.activeCollection.insert_one(entityObject.__dict__)
        
class BaseEntity(object):
    def __init__(self, **datas):
        self._id = datas.get("_id", newGUID())
        self.createDate = datas.get("_id", currentUTCDate())
        self.lastUpdateDate = datas.get("_id", currentUTCDate())

class Task(BaseEntity):
    def __init__(self, **datas):
        BaseEntity.__init__(self, **datas)
        self.taskData = datas.get("taskData", None)

myCollection = RepositoryCollection()

for i in range(20):
    myTask = Task()
    myCollection.insertOne(myTask)

print (myTask)