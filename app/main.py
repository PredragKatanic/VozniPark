from fastapi import FastAPI
from db import init_db
from api.routes import api_router

app = FastAPI()




@app.on_event("startup")
def startup_event():
    init_db()  # Inicijalizujte bazu podataka kada aplikacija počne sa radom

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(api_router)