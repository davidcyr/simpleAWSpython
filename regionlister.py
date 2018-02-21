import boto3

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
#print('Regions:', response['Regions'])

for region in response['Regions']:
     print(region['RegionName'])




