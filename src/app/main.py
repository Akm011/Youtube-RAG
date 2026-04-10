from fastapi import FastAPI
from app.api.routes import video, chat

app = FastAPI(title="YouTube RAG API", description="API for YouTube Retrieval-Augmented Generation", version="1.0.0")

app.include_router(video.router, prefix="/video", tags=["Video"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])