from src import init_app
from fastapi.middleware.cors import CORSMiddleware

app = init_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)