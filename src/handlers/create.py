import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('itemsTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        item_id = str(uuid.uuid4())
        name = body['name']

        table.put_item(
            Item={
                'id': item_id,
                'name': name
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Item created',
                'id': item_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
