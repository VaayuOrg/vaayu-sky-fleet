import os
from flask import Flask
from api import MissionRoutes, PilotRoutes, VehicleRoutes, UserRoutes

from factory.clients.mongo_client import MongoDBClient
from factory.clients.s3_client import S3Client

from dotenv import load_dotenv

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    
    # Initialize and register routes
    UserRoutes(app)
    PilotRoutes(app)
    VehicleRoutes(app)
    MissionRoutes(app)

    return app


# mongo_client = MongoDBClient()
# s3_client = S3Client()
# print(s3_client.create_bucket("sidak-fleet"))
# s3_client.list_buckets()

if __name__ == "__main__":
    load_dotenv()
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)
