from fastapi import FastAPI
from db.db import client
from controller.libroCRUD import router as librosRouter

app = FastAPI()
app.include_router(librosRouter, tags=["libros"], prefix="/libros")

# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

#Main para arrancar el server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0") #, port=8000, reload=True)
