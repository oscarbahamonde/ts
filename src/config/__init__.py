from os import getenv
from dotenv import load_dotenv
load_dotenv()
class process:
    class env:
        AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
        AWS_REGION = getenv("AWS_REGION")
        AWS_BUCKET_NAME = getenv("AWS_BUCKET_NAME")
        USER_POOL_ID = getenv("USER_POOL_ID")
        APP_CLIENT = getenv("APP_CLIENT")
        APP_CLIENT_SECRET = getenv("APP_CLIENT_SECRET")
        MAIL_FROM = getenv("MAIL_FROM") 
        MAIL_TO = getenv("MAIL_TO")
        PORT = getenv("PORT")
        REDIRECT_URI = getenv("REDIRECT_URI")
        TOKEN_URL = getenv("TOKEN_URL")
        ISSUER = getenv("ISSUER")
        JWKS_URL = getenv("JWKS_URL")
        HOSTED_UI = getenv("HOSTED_UI")
        POSTGRES_URI= getenv("POSTGRES_URI")
        CLIENT_URL = getenv("CLIENT_URL")
        