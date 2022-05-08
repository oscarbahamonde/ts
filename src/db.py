from .config import process
from sqlmodel import SQLModel, Field, create_engine, Session, Table
from fastapi import FastAPI

def init_db(app:FastAPI)->FastAPI:
    engine = create_engine(process.env.POSTGRES_URI)
    app.state.engine = engine
    app.state.session = Session(engine)
    app.state.session.autocommit = True
    @app.on_event("startup")
    def startup():
        SQLModel.metadata.create_all(engine)
        print('Database initialized')
        print(str(app.state.engine))
        print(str(app.state.session))
    @app.on_event("shutdown")
    def shutdown():
        app.state.session.close()
        print('Database closed')
    return app
