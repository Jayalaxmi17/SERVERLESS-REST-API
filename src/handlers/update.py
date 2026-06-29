import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('itemsTable')  # replace with your table

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        item_id = event['pathParameters']['id']
        name = body['name']

        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression="set #n = :name",
            ExpressionAttributeNames={
                '#n': 'name'
            },
            ExpressionAttributeValues={
                ':name': name
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Item updated successfully',
                'data': response
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
