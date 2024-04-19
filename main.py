from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from db.db import client
from controller.usuarioCRUD import router as usuarios_router

app = FastAPI()
app.include_router(usuarios_router, tags=["usuarios"], prefix="/usuarios")

# Handler para manejar excepciones y mostrarlas en pantalla
@app.exception_handler(HTTPException)
async def manejar_error_con_imagen(request : Request, exc :HTTPException ) -> HTMLResponse:
    url_imagen : str = f"https://http.cat/{exc.status_code}.jpg"
    return HTMLResponse(content=f"""
        <html>
            <head><title>Error {exc.status_code}</title></head>
            <body>
                <h1> Hubo un error :(</h1>
                <img src="{url_imagen}" alt="Imagen de error">
            </body>
        </html>
        """, status_code=exc.status_code)

# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

#Main para arrancar el server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
