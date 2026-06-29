import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('itemsTable')

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']

        table.delete_item(
            Key={'id': item_id}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
