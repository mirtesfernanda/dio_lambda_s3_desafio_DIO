
import json
import boto3
import os
import uuid

s3 = boto3.client('s3', endpoint_url=os.getenv('LOCALSTACK_URL', None))
dynamodb = boto3.resource('dynamodb', endpoint_url=os.getenv('LOCALSTACK_URL', None))
table_name = os.getenv('TABLE_NAME', 'UploadsMetadata')

def lambda_handler(event, context=None):
    print("Evento recebido:", json.dumps(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    size = event['Records'][0]['s3']['object'].get('size', 0)

    table = dynamodb.Table(table_name)
    item = {
        'id': str(uuid.uuid4()),
        'file_name': key,
        'bucket': bucket,
        'size': size
    }
    table.put_item(Item=item)

    print("Registro inserido com sucesso:", item)
    return {"statusCode": 200, "body": json.dumps("Processado com sucesso!")}
