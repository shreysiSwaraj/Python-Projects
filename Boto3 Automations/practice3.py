#script to launch an ec2 instance

import boto3

aws_console = boto3.session.Session(profile_name='default')

ec2 = boto3.client('ec2')

# stooping an instance
# response = ec2.stop_instances(
#     InstanceIds = ['string']
# )

#starting an instance
#
# terminating an instance
response = ec2.terminate_instances(
    InstanceIds = ['string']
)

