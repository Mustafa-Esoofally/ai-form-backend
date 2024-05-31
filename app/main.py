import os

os.environ['OPENAI_API_KEY'] = 'sk-proj-MoIPCe9jvmJEAQ9TtCCaT3BlbkFJoiSBwjwGSbpZh0K1AX3n'

# Your code here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.address_chunk import address_chunk_router
from app.routes.save_address import save_address_router


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(address_chunk_router)
app.include_router(save_address_router)