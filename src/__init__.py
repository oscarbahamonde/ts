from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from .cognito import auth
from .s3 import s3_router
from .ses import ses_router

app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.include_router(auth, prefix='/auth')
app.include_router(s3_router, prefix='/s3')
app.include_router(ses_router, prefix='/ses')

@app.get('/')
async def root(req:Request):
    return templates.TemplateResponse('index.html', {'request': req})

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)