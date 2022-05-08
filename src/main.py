from .config import process
from boto3 import client, resource

def getClient(service:str):
    return client(
        service,
        aws_access_key_id=process.env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=process.env.AWS_SECRET_ACCESS_KEY,
        region_name=process.env.AWS_REGION
    )

def getResource(service:str):
    return resource(
        service,
        aws_access_key_id=process.env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=process.env.AWS_SECRET_ACCESS_KEY,
        region_name=process.env.AWS_REGION
    )
