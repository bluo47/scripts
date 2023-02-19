import boto3
import os

AWS_KEY_ID = os.environ.get("AWS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME")

session = boto3.Session(
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

s3 = session.client('s3')
# s3 = boto3.client('s3')

file_name = 'D:\Demo\datafile\dprfile02.txt'
object_name = 'ben2023/dprfile02.txt'

# Upload the file
# s3.upload_file(file_name, AWS_S3_BUCKET_NAME, object_name)
try:
    s3.upload_file(file_name, AWS_S3_BUCKET_NAME, object_name)
    # print("File uploaded successfully!")
    print(f"File '{file_name}' uploaded successfully.")
    print(f"S3 '{object_name}' ")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"Upload failed: {e}")
