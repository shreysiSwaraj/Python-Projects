#script to print instance id of all the ec2 instances
import boto3

aws_management_console = boto3.session.Session(profile_name='default')

ec2 = aws_management_console.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations'] :
    for instance in reservation['Instances'] :
        #print(instance)
        instance_id = instance['InstanceId']
        print(instance_id)