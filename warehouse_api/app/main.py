from fastapi import FastAPI
from app.database import Base,engine
from app.models.warehouse import Warehouse

Base.metadata.create_all(bind=engine) #here we create the table that we mention in models

app = FastAPI(
    title="Warehouse API",
    version="1.0.0",
)

@app.get("/")
def root():
    return{
        'message':'Warehouse API is running'
    }