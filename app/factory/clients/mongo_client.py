import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# connects to mongodb-atlas and defines mongo operations
class MongoDBClient:
    def __init__(self):
        load_dotenv()
        self.mongo_uri = os.getenv("MONGO_URI")

        if not self.mongo_uri:
            raise ValueError("❌ MONGO_URI is not set in the .env file")

        self.client = self._connect_to_client()

    def _connect_to_client(self):
        try:
           client = MongoClient(self.mongo_uri, server_api=ServerApi('1'))
           client.admin.command('ping')
           print("Pinged your deployment. You successfully connected to MongoDB!")
           return client
        except Exception as e:
           print(e)

    def close_connection(self):
        if self.client:
            self.client.close()
            print("🔌 MongoDB connection closed.")       

    def create_database(self, db_name: str):
        if self.client:
            db_name = self.client[db_name]
            print(f"📂 Database created")
            return db_name
        else:
            print("DB not connected")
            # raise ConnectionError("❌ MongoDB client not initialized.")
            return None

    def delete_database(self, db_name):
        if self.client:
            self.client.drop_database(db_name)
            print(f"🗑️ Database '{db_name}' deleted.")
        else:
            print("DB not connected")
            # raise ConnectionError("❌ MongoDB client not initialized.")
            return None

    def insert(self, db_name : str,  collection_name : str, data):
        try:
            collection = db_name[collection_name]
            result = collection.insert_one(data)
            print(f"✅ Data inserted into {collection_name} with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"❌ Failed to insert data into: {e}")
            return None        
    
    def read(self, db_name : str, collection_name: str, query: dict = {}):
        try:
            collection = db_name[collection_name]
            results = list(collection.find(query))
            print(f"📄 Found {len(results)} document(s) in '{collection_name}'")
            return results
        except Exception as e:
            print(f"❌ Failed to read data from {collection_name}: {e}")
            return None

    def update(self, db_name : str, collection_name: str, query: dict, update_data: dict):
        try:
            collection = db_name[collection_name]
            result = collection.update_many(query, {'$set': update_data})
            print(f"🔄 Updated {result.modified_count} document(s) in '{collection_name}'")
            return result.modified_count
        except Exception as e:
            print(f"❌ Failed to update documents in {collection_name}: {e}")
            return None

    def delete(self, db_name : str, collection_name: str, query: dict):
        try:
            collection = db_name[collection_name]
            result = collection.delete_many(query)
            print(f"🗑️ Deleted {result.deleted_count} document(s) from '{collection_name}'")
            return result.deleted_count
        except Exception as e:
            print(f"❌ Failed to delete documents from {collection_name}: {e}")
            return None
