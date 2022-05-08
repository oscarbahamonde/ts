from .main import getClient, getResource
from fastapi import APIRouter, Request
from .config import process
from .schemas import ContactForm

client = getClient("ses")
ses = APIRouter()

@ses.post("/send")
async def send(form: ContactForm):
    # Send email
    response = client.send_email(
        Source=process.env.MAIL_FROM,
        Destination={
            'ToAddresses': [
                process.env.MAIL_TO
            ]
        },
        Message={
            'Subject': {
                'Data': f'{form.name}<{form.email}> sent you a message'
            },
            'Body': {
                'Text': {
                    'Data': form.message
                }
            }
        }
    )
    return response