import boto3

AWS_REGION = "sa-east-1"

client = boto3.client('s3', aws_access_key_id='as6d5a65d1a65',
    aws_secret_access_key='651da65d1as', region_name=AWS_REGION)

resource = boto3.resource('s3')

response = client.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]


def printAllBuckets():
    print('Existing buckets:')
    print(buckets)

def creatBucket():
    newBucket = input('Dê um nome ao novo bucket a ser criado na nuvem: ')
    response = client.create_bucket(Bucket=newBucket)
    print("Bucket criado com sucesso!")
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print('Existing buckets:')
    print(buckets)

def conteudoBucket():
    bucket_name = 'balde.01'
    response = client.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print('Bucket vazio.')

def addFile():
    file_name = 'C:\\Users\\guiga\\Desktop\\Pasta\\ListaPaises.txt'
    bucket_name = 'balde.01'

    with open(file_name, "rb") as f:
        client.upload_fileobj(f, bucket_name, file_name)
    print('Arquivo enviado à nuvem.')

def deleteFile():
    bucket_name = 'balde.01'
    file_name = 'C:\\Users\\guiga\\Desktop\\Pasta\\ListaPaises.txt'
    client.delete_object(Bucket=bucket_name, Key=file_name)
    print('Arquivo deletado da nuvem.')


printAllBuckets()
conteudoBucket()
addFile()
#deleteFile()
conteudoBucket()
