import boto3
import os
AWS_KEY_ID = os.environ.get("AWS_KEY_ID_SL")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY_SL")
session = boto3.Session(
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
# AWS account
print(AWS_KEY_ID)

#########################################################
# Caution: This script will terminate all the EC2
#########################################################
region = 'us-east-1'
ec2 = session.client('ec2', region_name=region)
response = ec2.describe_instances()

# Loop through the reservations in the response and extract information about the instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Public IP: {instance.get('PublicIpAddress', '-')}")
        # Terminate the instance
        response = ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
        print(response)

