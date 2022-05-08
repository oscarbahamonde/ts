from fastapi import APIRouter, FastAPI
from fastapi.exceptions import HTTPException
from jose import jwt
from requests import post
from starlette.responses import RedirectResponse
from .config import process
from .models import Profile

auth = APIRouter()


def init_auth(app:FastAPI)->FastAPI:
    @auth.get('/token')
    async def get_token(code:str):
        return RedirectResponse(f'{process.env.CLIENT_URL}profile?id={code}')
    @auth.post('/token')
    def getUnverifiedClaims(code:str):
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': process.env.REDIRECT_URI,
            'client_id': process.env.APP_CLIENT,
            'client_secret': process.env.APP_CLIENT_SECRET
        }
        token = post(process.env.TOKEN_URL, data=data).json()['id_token']
        claims = jwt.get_unverified_claims(token)
        user = {
            'id': claims['sub'],
            'username': claims['cognito:username'],
            'email': claims['email'],
            'token': token
        }
        return user

    @auth.post('/user/update')
    def create_or_update_profile(profile:Profile):
        if (app.state.session.query(Profile).filter(Profile.id == profile.id).first()):
            try:
                app.state.session.query(Profile).filter(Profile.id == profile.id).update(profile.dict())
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        elif (profile.id):
            try:
                app.state.session.add(profile)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        else:
            raise HTTPException(status_code=400, detail='Profile id is required')
        return profile
    app.include_router(auth, prefix="/auth")
    return app