from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """ #describe purpose of module

    def __init__(self, username, password): #names function and lists arguments 
        self.client = MongoClient('mongodb://%s:%s@localhost:36015' % (username, password))
        self.database = self.client['AAC'] #database used
        
# Create method to implement the C in CRUD.
    def create(self, data): #names function and lists arguments
        if data is not None:
            self.database.animals.insert(data)  # inserts data   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty") #data is none
            return False

# Create method to implement the R in CRUD. 
    def read(self, data): #names function and lists arguments
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
            #return self.database.animals.find(data) #finds and returns data
        else:
            raise Exception("Nothing to search, because data parameter is empty") #data is none
            return False
        
# Create method to implement the U in CRUD
    def update(self, data, newData):
        if data is not None:
            result = self.database.animals.update(data, newData) #take old data and change into new data
            return dumps(self.read(newData)) #return new data
        else:
            raise Exception("Nothing to update, because data parameter is empty") #data is none
            return False
        
#Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            #return dumps(self.read(data))
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty") #data is none
            return False
