import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('scratch_questions')


# note that table.put_item() is an insert or overwrite


r1 = table.put_item(
    Item={
        'quiz_id' : '1',
        'question_number' : 1,
        'question_text' : 'Which is the correct answer?',
        'option_1' : 'Not this one.',
        'option_2' : 'This is the correct answer.',
        'option_3' : 'Nope, not this one.',
        'option_4' : 'Not this one either.',
        'correct_option' : 2
    }
)

print(r1)

r2 = table.put_item(
    Item={
        'quiz_id' : '1',
        'question_number' : 2,
        'question_text' : 'Here''s another one.',
        'option_1' : 'This is the correct answer.',
        'option_2' : 'Not this one.',
        'option_3' : 'Nope, not this one.',
        'option_4' : 'Not this one either.',
        'correct_option' : 1
    }
) 

print(r2)
