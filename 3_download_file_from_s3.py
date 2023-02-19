import boto3
import os

AWS_KEY_ID = os.environ.get("AWS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET_NAME")

session = boto3.Session(
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

print(AWS_S3_BUCKET_NAME)
s3 = session.client('s3')
# s3 = boto3.client('s3')

file_name = 'D:\Demo\datafile\dprfile02.txt'
object_name = 'ben2023/dprfile02.txt'
file_name4download = 'D:\Demo\datafile\dprfile02_download.txt'

# Download the file
try:
    # Download the file from S3
    s3.download_file(AWS_S3_BUCKET_NAME, object_name, file_name4download)
    print(f"File '{file_name4download}' downloaded successfully.")
except Exception as e:
    print(f"Download failed: {e}")