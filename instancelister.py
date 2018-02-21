import boto3

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
#print('Regions:', response['Regions'])

for region in response['Regions']:
     print(region['RegionName'])
     regionalEc2 = boto3.client('ec2',region_name=region['RegionName'])
     regionalInstances = regionalEc2.describe_instances()
     reservations = regionalInstances['Reservations']
     for r in reservations:
        for i in r['Instances']:
             #print(i)
             #
             # TODO - print a few interesting fields, and also get at TAGs
             #
             print('   ' + i['InstanceId'])






