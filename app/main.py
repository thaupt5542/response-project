from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

fake_items_db = ("a":"b"::"c")

@app.get("/")
def root():
    return { "time": datetime.now() }

 @app.get("/")
    ...: async def root():
    ...:     return {"message": "Hello World"}  
 
