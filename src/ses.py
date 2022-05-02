from .api import api
from fastapi import APIRouter

ses = api.getclient(service='ses')
ses_router = APIRouter()
@ses_router.post('/')
async def sendEmail(email:str, body:str):
    response = ses.send_email(
        Source=api._ses_mail_from,
        Destination={
            'ToAddresses': [
                api._ses_mail_to
            ]
        },
        Message={
            'Subject': {
                'Data': 'mail from ' + email
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
    return response