from fastapi import FastAPI
from models.user import User
from fastapi import Body
from typing import Annotated
from db.conn import connect_to_mongodb
from db.conn import conn
from controllers.user import router
import uvicorn
connect_to_mongodb()
from models.user import create_tables;
conn()
create_tables()

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
   