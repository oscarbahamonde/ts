from .api import api
from fastapi import APIRouter

s3 = api.getclient(service='s3')
s3_router = APIRouter()
@s3_router.get('/bucket')
async def listObjects(id:str):
    response = s3.list_objects(Bucket=api._bucket, Prefix=id)
    return response
@s3_router.get('/url')
async def getUrl(key:str, id:str):
    response = s3.generate_presigned_url('get_object', Params={'Bucket': api._bucket, 'Key': key, 'Prefix': id, 'acl': 'public-read'})
    return response