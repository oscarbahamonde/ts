from fastapi import APIRouter
from pydantic import BaseModel
from jose import jwt
from requests import post
from starlette.responses import RedirectResponse
from .api import api

auth = APIRouter()
@auth.get('/token')
async def getUser(code:str)->BaseModel:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': api._cognito_app_client,
        'client_secret': api._cognito_app_client_secret,
        'code': code,
        'redirect_uri': api._cognito_redirect_url
    }
    response = post(api._token_url, headers=headers, data=data).json()
    claims = jwt.get_unverified_claims(response['id_token'])
    res = {
        'id': claims['sub'],
        'username': claims['cognito:username'],
        'email': claims['email'],
        'token': response['id_token']
    }
    return RedirectResponse(f'{api._nuxt_app_url}/profile?id={res["id"]}&username={res["username"]}&email={res["email"]}&token={res["token"]}')