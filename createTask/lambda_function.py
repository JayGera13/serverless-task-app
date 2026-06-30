import json
import boto3
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Tasks')
    
    body = json.loads(event['body'])
    
    task = {
        'taskID': str(uuid.uuid4()),
        'title': body['title'],
        'done': False
    }
    
    table.put_item(Item=task)
    
    return {
    'statusCode': 201,
    'headers': {
        'Access-Control-Allow-Origin': '*'
    },
    'body': json.dumps(task)
}