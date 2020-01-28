from pymongo import MongoClient
import bd-finance-project-server.appSettings
import bson

def newGUID():
    import uuid
    return str(uuid.uuid4())

def currentUTCDate():
    import datetime
    return datetime.datetime.utcnow()

def getConnectionString():
    import appSettings
    return appSettings.MONGO_CONN_STRING

class RepositoryCollection():
    def __init__(self, collectionName = "Task"):
        myClient = MongoClient(host = getConnectionString())
        self.database = myClient["financial_data"]
        self.activeCollection = self.database[collectionName]
        
    def insertOne(self, entityObject):
        assert isinstance(entityObject, BaseEntity)
        self.activeCollection.insert_one(entityObject)
        
class BaseEntity(object):
    def __init__(self, **datas):
        self._id = datas.get("_id", newGUID())
        self.createDate = datas.get("_id", currentUTCDate())
        self.lastUpdateDate = datas.get("_id", currentUTCDate())
    
class Task(BaseEntity):
    def __init__(self, **datas):
        BaseEntity.__init__(self, **datas)
        self.taskData = datas.get("taskData", None)

myTask = Task(taskData = "Hello World")

myCollection = RepositoryCollection()
myCollection.insertOne(myTask)

print (myTask)