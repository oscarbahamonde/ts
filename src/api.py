from dotenv import load_dotenv
load_dotenv()
from os import getenv
from boto3 import client

class API ():
    def __init__(self):
        self._access_key:str = getenv("AWS_ACCESS_KEY_ID")
        self._secret_key:str = getenv("AWS_SECRET_ACCESS_KEY")
        self._region:str = getenv("AWS_REGION")
        self._bucket:str = getenv("AWS_BUCKET_NAME")
        self._cognito_user_pool_id:str = getenv("AWS_USER_POOL_ID")
        self._cognito_hosted_ui:str = getenv("AWS_HOSTED_UI")
        self._cognito_redirect_url:str = getenv("AWS_REDIRECT_URL")
        self._cognito_app_client:str = getenv("AWS_APP_CLIENT")
        self._cognito_app_client_secret:str = getenv("AWS_APP_CLIENT_SECRET")
        self._ses_mail_from:str = getenv("AWS_MAIL_FROM")
        self._ses_mail_to:str = getenv("AWS_MAIL_TO")
        self._token_url:str = getenv("AWS_ACCESS_TOKEN_URL")
        self._nuxt_app_url:str = getenv("CLIENT_URL")

    def getclient(self, service:str):
        return client(service, 
            aws_access_key_id=self._access_key,
            aws_secret_access_key=self._secret_key,
            region_name=self._region,
        )

api = API()