from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import profile, user

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Job Application Assistant is running"}