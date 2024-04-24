from fastapi import HTTPException, APIRouter
from db.db import collection 
from model.usuario import Usuario
from pymongo import results

router : APIRouter = APIRouter()

#Crea un usuario
@router.post('/', response_description="Crear nuevo usuario", response_model= Usuario)
async def createUsuario(usuario : Usuario) -> Usuario:
    existingUser : Usuario | None = await collection.find_one({"email" : usuario.email})
    if existingUser:
        raise HTTPException(status_code = 226, detail = "El email ya existe")
    result : results.InsertOneResult = await collection.insert_one(usuario.model_dump())
    usuario._id = str(result.inserted_id)
    return usuario

#Obtiene la lista de todos los usuarios
@router.get('/', response_description="Obtener usuarios", response_model= list[Usuario])
async def readUsuarios() -> list[Usuario]:
    usuarios : list[Usuario] = await collection.find().to_list(100)
    for usuario in usuarios:
        print(usuario)
    return usuarios

#Obtiene un usuario por email y actualiza sus valores
@router.put('/{email}', response_description="Actualizar usuario por email", response_model= Usuario)
async def updateUsuario(email : str, userToUpdate : Usuario) -> Usuario:
    updatedUser : Usuario | None = await collection.find_one_and_update({"email" : email}, {"$set" : userToUpdate.model_dump()})
    if not updatedUser:
        raise HTTPException(status_code = 304, detail = "El usuario no existe")
    return updatedUser

#Obtiene un usuario por email
@router.get('/{email}', response_description="Obtener usuario por email", response_model= Usuario)
async def findUsuarioByEmail(email : str) -> Usuario:
    user : Usuario | None = await collection.find_one({"email" : email})
    if not user:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    return user

#Obtiene un usuario por email y lo elimina
@router.delete('/{email}', response_description="Borrar usuario por email", response_model= Usuario)
async def deleteUsuario(email : str) -> Usuario:
    deletedUser : Usuario | None = await collection.find_one_and_delete({"email" : email})
    if not deletedUser:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    return deletedUser

