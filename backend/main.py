from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from methods import users, rooms


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/users', users)
app.mount('/rooms', rooms)
