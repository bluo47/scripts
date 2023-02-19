import boto3
import os

region = 'us-east-1'
AWS_KEY_ID = os.environ.get("AWS_KEY_ID_SL")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY_SL")
session = boto3.Session(
    region_name= region,
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
# AWS accoount
print(AWS_KEY_ID)

ec2 = session.resource('ec2')
# ec2 = boto3.resource('ec2')

# Create a new Ubuntu instance
instance = ec2.create_instances(
    ImageId='ami-0dba2cb6798deb6d8',  # Ubuntu Server 20.04 LTS
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='triotemp',
    SecurityGroups=['default']
    # SecurityGroupIds=[security_group.group_id]
)

# Wait for the instance to be running
instance[0].wait_until_running()

# Print the public IP address of the instance
print(instance[0].public_ip_address)
