from fastapi import FastAPI, Request
from .contact import ses as contact
from .drive import s3 as drive
from .auth import init_auth
from .db import init_db
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

def init_app():
    _app=FastAPI()
    app = init_auth(init_db(_app))
    app.include_router(contact, prefix="/contact")
    app.include_router(drive, prefix="/drive")
    @app.get("/")
    async def root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})
    app.mount("/hhmc", StaticFiles(directory="templates"), name="static")
    return app

