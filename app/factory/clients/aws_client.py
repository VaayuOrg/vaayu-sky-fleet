import boto3
import os
from dotenv import load_dotenv

# connects to the instance of aws-iam user ie "user-vaayu"
class AWSClient:
    def __init__(self):
        load_dotenv()
        self.access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.region = os.getenv("AWS_REGION")
        # self.bucket_name = os.getenv("S3_BUCKET_NAME")  
        # would be an user input and names should be globally unique and lowercase without special characters

        self.user = self._connect_to_aws()

    def _connect_to_aws(self):
        try:
            user = boto3.client(
                's3',
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name=os.getenv("AWS_REGION")
            )
            print("✅ Connected to AWS S3")
            return user
        except Exception as e:
            print(f"❌ Failed to connect to S3: {e}")
            return None
