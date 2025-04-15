import os
from flask import Flask
from database.clients.mongo_client import MongoDBClient
from database.clients.s3_client import S3Client
from dotenv import load_dotenv

app = Flask(__name__)

# mongo_client = MongoDBClient()
s3_client = S3Client()
print(s3_client.create_bucket("sidak-fleet"))
s3_client.list_buckets()

# if __name__ == "__main__":
    # load_dotenv()
    # app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
