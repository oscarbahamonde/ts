from fileinput import filename
from fastapi import APIRouter, File, UploadFile, Depends
from .main import getClient
from .config import process

s3 = APIRouter()
client = getClient("s3")
bucket = process.env.AWS_BUCKET_NAME

@s3.post('/upload')
async def upload(id:str, file: UploadFile = File(...)):
    payload = file.file.read()
    client.put_object(
        Bucket=bucket,
        Key=f"{id}/{file.filename}",
        Body=payload
    )
    return {"url": f"https://{bucket}.s3.{process.env.AWS_REGION}.amazonaws.com/{id}/{file.filename}"}