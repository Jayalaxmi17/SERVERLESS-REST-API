# File: src/auth/authorizer.py
import os
import boto3
import jwt

ssm = boto3.client('ssm', region_name='ap-south-1')

def get_secret(param_name):
    response = ssm.get_parameter(Name=param_name, WithDecryption=True)
    return response['Parameter']['Value']

SECRET = get_secret(os.environ['JWT_SECRET_PARAM'])

def handler(event, context):
    try:
        token = event.get('authorizationToken', '').replace('Bearer ', '')
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        effect = 'Allow'
    except Exception as e:
        print(f'Auth error: {str(e)}')
        effect = 'Deny'
        payload = {}

    return {
        'principalId': payload.get('user_id', 'user'),
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': event['methodArn'].rsplit('/', 3)[0] + '/*/*'
            }]
        }
    }
