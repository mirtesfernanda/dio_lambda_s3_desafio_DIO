
#!/bin/bash
echo "Criando recursos no LocalStack..."

awslocal s3 mb s3://lambda-s3-upload-bucket
awslocal dynamodb create-table         --table-name UploadsMetadata         --attribute-definitions AttributeName=id,AttributeType=S         --key-schema AttributeName=id,KeyType=HASH         --billing-mode PAY_PER_REQUEST

echo "Recursos criados com sucesso!"
