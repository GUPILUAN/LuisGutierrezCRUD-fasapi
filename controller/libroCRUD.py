from fastapi import HTTPException, APIRouter
from db.db import collection 
from model.libro import Libro
from pymongo import results

router : APIRouter = APIRouter()

#Crea un libro
@router.post('/', response_description= "Crear nuevo libro", response_model= Libro)
async def createLibro(libro : Libro) -> Libro:
    existingLibro : Libro | None = await collection.find_one({"isbn" : libro.autor})
    if existingLibro:
        raise HTTPException(status_code= 226, detail= "El isbn ya existe")
    result : results.InsertOneResult = await collection.insert_one(libro.model_dump())
    libro._id = str(result.inserted_id)
    return libro

#Obtiene la lista de todos los libros
@router.get('/', response_description= "Obtener libros", response_model= list[Libro])
async def readLibros() -> list[Libro]:
    libros : list[Libro] = await collection.find().to_list(100)
    for libro in libros:
        print(libro)
    return libros

#Obtiene un libro por isbn y actualiza sus valores
@router.put('/{isbn}', response_description= "Actualizar libro por isbn", response_model= Libro)
async def updateLibro(isbn : str, libroToUpdate : Libro) -> Libro:
    updatedLibro : Libro | None = await collection.find_one_and_update({"isbn" : isbn}, {"$set" : libroToUpdate.model_dump()})
    if not updatedLibro:
        raise HTTPException(status_code= 304, detail= "El libro no existe")
    return updatedLibro

#Obtiene un libro por isbn
@router.get('/{isbn}', response_description= "Obtener libro por isbn", response_model= Libro)
async def findLibroByIsbn(isbn : str) -> Libro:
    libro : Libro | None = await collection.find_one({"isbn" : isbn})
    if not libro:
        raise HTTPException(status_code= 404, detail= "El libro no existe")
    return libro

#Obtiene un libro por isbn y lo elimina
@router.delete('/{isbn}', response_description= "Borrar libro por isbn", response_model= Libro)
async def deleteLibro(isbn : str) -> Libro:
    deletedLibro : Libro | None = await collection.find_one_and_delete({"isbn" : isbn})
    if not deletedLibro:
        raise HTTPException(status_code= 404, detail= "El libro no existe")
    return deletedLibro

