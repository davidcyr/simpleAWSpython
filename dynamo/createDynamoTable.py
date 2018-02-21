import boto3


dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName = 'scratch_questions',
    KeySchema = [
        {
            'AttributeName' : 'quiz_id',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'question_number',
            'KeyType' : 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName' : 'quiz_id',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'question_number',
            'AttributeType' : 'N'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits' : 5,
        'WriteCapacityUnits' : 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='scratch_questions')

# Print out some data about the table.
print(table.item_count)


