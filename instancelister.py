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
             # Tags take a bit of effort since they are an array of objects
             # but we should be putting a human readable description in the Name tag
             # so it's likely worth getting for display
	     instanceName = ''
             if 'Tags' in i.keys():
                 for tags in i['Tags']:
                     if tags['Key'] == 'Name':
                         instanceName = tags['Value']

	     oString = '    {}  ({})  {}'
	     
             print(oString.format(
                 i['InstanceId'], 
                 i['State']['Name'],
		 instanceName
		 )
	     )







