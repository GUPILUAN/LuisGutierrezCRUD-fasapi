from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from db.db import client
from controller.usuarioCRUD import router as usuarios_router

app = FastAPI()
app.include_router(usuarios_router, tags=["usuarios"], prefix="/usuarios")

# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

#Main para arrancar el server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0") #, port=8000, reload=True)
