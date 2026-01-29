#script for creating an ec2 instance

import boto3

aws_console = boto3.session.Session(profile_name='default')

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='string',
    InstanceType='a1.medium',
    MaxCount=1,
    MinCount=1
)