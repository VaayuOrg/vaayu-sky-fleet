import os
from botocore.exceptions import NoCredentialsError, ClientError
from factory.clients.aws_client import AWSClient

# inovokes aws_client and uses it to define S3 operations
class S3Client():
    def __init__(self):
        self.aws_client = AWSClient()

    def upload_file(self, file_path, s3_file_name=None):
        if not s3_file_name:
            s3_file_name = os.path.basename(file_path)
        try:
            self.aws_client.user.upload_file(file_path, self.bucket_name, s3_file_name)
            print(f"✅ File uploaded successfully as '{s3_file_name}' in bucket '{self.bucket_name}'")
            return True
        except FileNotFoundError:
            print("❌ File not found.")
        except NoCredentialsError:
            print("❌ AWS credentials not available.")
        except ClientError as e:
            print(f"❌ Upload failed: {e}")
        return False
    
    def create_bucket(self, bucket_name):
        if not self.aws_client.user:
            print("❌ aws client not initialized.")
            return None

        try:
            if self.aws_client.region == "us-east-1":
                  response = self.aws_client.user.create_bucket(Bucket=bucket_name)
            else:
                response = self.aws_client.user.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.aws_client.region}
                )
            print(f"✅ Bucket '{bucket_name}' created successfully.")
            return response
        except ClientError as e:
            print(f"❌ Failed to create bucket: {e}")
            return None
        
    def list_buckets(self):
        try:
            response = self.aws_client.user.list_buckets()
            bucket_names = [bucket['Name'] for bucket in response.get('Buckets', [])]
            print("✅ Buckets found:", bucket_names)
            return bucket_names
        except Exception as e:
            print(f"❌ Failed to list buckets: {e}")
            return None
    
