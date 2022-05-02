from dotenv import load_dotenv
load_dotenv()
from os import getenv
from fastapi import APIRouter
from jose import jwt
from requests import post
from starlette.responses import RedirectResponse

auth = APIRouter()

AWS_CLIENT_ID = getenv('AWS_APP_CLIENT')
AWS_CLIENT_SECRET = getenv('AWS_APP_CLIENT_SECRET')
AWS_REGION = getenv('AWS_REGION')
AWS_USER_POOL_ID = getenv('AWS_USER_POOL_ID')
AWS_HOSTED_UI= getenv('AWS_HOSTED_UI')
AWS_ACCESS_TOKEN_URL = getenv('AWS_ACCESS_TOKEN_URL')
AWS_REDIRECT_URL = getenv('AWS_REDIRECT_URL')
CLIENT_URL = getenv('CLIENT_URL')
async def AuthCodeToAccessToken(code:str)->str:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': AWS_CLIENT_ID,
        'client_secret': AWS_CLIENT_SECRET,
        'code': code,
        'redirect_uri': AWS_REDIRECT_URL
    }
    response = post(AWS_ACCESS_TOKEN_URL, headers=headers, data=data)
    return response.json()

@auth.get('/token')
async def get_token(code:str):
    user = await AuthCodeToAccessToken(code)
    claims = jwt.get_unverified_claims(user['id_token'])
    res = {
        'id': claims['sub'],
        'username': claims['cognito:username'],
        'email': claims['email'],
        'token': user['id_token']
    }
    return RedirectResponse(f'{CLIENT_URL}/profile?id={res["id"]}&username={res["username"]}&email={res["email"]}&token={res["token"]}')
