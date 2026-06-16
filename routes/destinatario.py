from fastapi import APIRouter
from models.destinatario import Destinatario, DestinatarioGet, DestinatarioCreate, DestinatarioUpdate
from repositories.carrera_db import obtener_carreras_id
from repositories.destinatario_db import crear_destinatario, obtener_destinatario_por_dni,obtener_todos_destinatarios, eliminar_destinatario, modificar_destinatario, obtener_destinatario_id
from fastapi.responses import JSONResponse

# routes/destinatario.py
router = APIRouter(prefix="/destinatario", tags=["Destinatarios"])

@router.get("/", response_model=list[DestinatarioGet])
def obtener_destinatarios():
    destinatarios = obtener_todos_destinatarios()
    
    return(destinatarios)
@router.get("/{id}" , response_model=DestinatarioGet, status_code=200)
def obtener_destinatario_id_route(id:int):
    destinatario = obtener_destinatario_id(id)
    return(destinatario)

@router.post("/", response_model=dict)
def agregar_destinatario_route(dest: DestinatarioCreate):
    if dest.id_carrera:
        carrera = obtener_carreras_id(dest.id_carrera)
        if not carrera:
            return JSONResponse({"mensaje": "La carrera con el id proporcionado no existe"}, status_code=404)

    # verificar si el dni ya existe
    destinatario_existente = obtener_destinatario_por_dni(dest.dni)
    if destinatario_existente:
        return JSONResponse({"mensaje": "Ya existe un destinatario con ese DNI"}, status_code=400)


    if crear_destinatario(dest):
        return JSONResponse({"mensaje": "Destinatario creado"}, status_code=201)
    return JSONResponse({"mensaje": "Error al crear el destinatario"}, status_code=500)


@router.delete("/{id}", status_code=200)
def eliminar_destinatario_route(id: int):
    destinatario = obtener_destinatario_id(id)
    if destinatario:
        eliminar_destinatario(destinatario)
        return {"mensaje": "Destinatario eliminado"}
    return {"mensaje": "Destinatario NO encontrado"}

@router.put("/{id}", status_code=200)
def modificar_destinatario_route(id : int, nuevo_dest : DestinatarioUpdate)-> dict: 
    destinatario = obtener_destinatario_id(id)
    if destinatario:
        modificar_destinatario(id, nuevo_dest)
        return {"mensaje": "Destinatario modificado"}
    
    return {"mensaje": "Destinatario NO encontrado"}    