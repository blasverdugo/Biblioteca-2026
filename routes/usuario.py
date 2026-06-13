from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
#from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from datetime import timedelta

# Importa tus modelos y configuración desde su ubicación real
from models.usuario import Usuario, UserCreate, UserPublic, UserUpdate, PasswordUpdate
from repositories.insumo_db import crear_usuario, obtener_todos_usuario, eliminar_usuario, modificar_usuario, obtener_usuario_dni #FALTA HACER EN REPOSITORES
from database.db import get_db

#FALTA HACER EL SERVICE
from services.user_services import (
    obtener_password_hash,
    verificar_password,
    crear_token_acceso,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/users", tags=["Users"])

# End points publicos (sin autorizacion)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def registrar_usuario(
    usuario_in: UserCreate,
    db: Annotated[Session, Depends(get_db)]
):
    #verificar que el username no exista
    statement_username = select(Usuario).where(Usuario.username == usuario_in.username)
    if db.exec(statement_username).first():
        raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="El nombre de usuario ya esta registrado",
        )
    #validar el gmail
    statement_email = select(Usuario).where(Usuario.email == usuario_in.email)
    if db.exec(statement_email).first():
        raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="El gmail ya esta registrado",
        )
    
    # Encriptar el nuevo usuario
    nuevo_user = Usuario(
        username = usuario_in.username,
        email= usuario_in.email,
        nombre= usuario_in.nombre,
        apellido=usuario_in.apellido,
        password_hashed=obtener_password_hash(usuario_in.password_hashed),
        disabled=False,
    )
    db.add(nuevo_user)
    db.commit()
    db.refresh(nuevo_user)
    
    return {"mensaje" : "usuario registrado perrrooooooo"}

@router.post("/login")
async def login_para_obtener_token(
    form_data:Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    #Endpoint para autenticarse e intercambiar credenciales por un JWT.
    statement = select(Usuario).where(Usuario.username == form_data.username)
    user = db.exec(statement).first()
    
    if not user or not verificar_password(form_data.password, user.password_hashed):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contrasenia incorrecta",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crear_token_acceso(
        data={"sub": user.username}, expires_delta= access_token_expires
    )
    
    return {"access_token": access_token, "token_type":"bearer"}

    #JWT (Json Web Token) contiene informacion codificada
    

        
