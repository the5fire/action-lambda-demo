import json

import requests


def lambda_handler(event, context):
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

    return {
        'statusCode': 200,
        'body': json.dumps({'content': f'hi the5fire, code:{r.status_code}'})
    }

