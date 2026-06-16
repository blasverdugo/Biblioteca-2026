from fastapi import APIRouter
from models.carrera import Carrera, CarreraGet, CarreraCreate, CarreraUpdate
from repositories.carrera_db import crear_carrera, obtener_todas_las_carreras, eliminar_carrera, modificar_carrera, obtener_carreras_id



# routes/carrera.py
router = APIRouter(prefix="/carrera", tags=["Carreras"])

@router.get("/", response_model=list[CarreraGet])
def obtener_carreras():
    carreras = obtener_todas_las_carreras()
    return carreras

@router.get("/{id}", response_model=CarreraGet)
def obtener_carrera_id(id: int):
    carrera = obtener_carreras_id(id)
    return carrera

@router.post("/", status_code=201, response_model=CarreraGet)
def crear_carrera_route(carrera: CarreraCreate):
    return crear_carrera(carrera)

@router.delete("/{id}", status_code=200)
def eliminar_carrera_route(id: int):
    carrera = obtener_carreras_id(id)
    if carrera:
        eliminar_carrera(carrera)
        return {"mensaje": "Carrera eliminada"}
    return {"mensaje": "Carrera NO encontrada"}

@router.put("/{id}", status_code=200)
def modificar_carrera_route(id: int, nueva_carrera: CarreraUpdate):
    carrera = obtener_carreras_id(id)
    if carrera:
        modificar_carrera(id, nueva_carrera)
        return {"mensaje": "Carrera modificada"}
    return {"mensaje": "Carrera NO encontrada"}

@router.get("/{id}" , response_model=CarreraGet, status_code=200)
def obtener_carrera_id_route(id:int):
    carrera = obtener_carrera_id(id)
    return(carrera)

@router.post("/", status_code=201, response_model=CarreraGet)
def agregar_carrera_route(carrera: CarreraCreate):
    return crear_carrera(carrera)


@router.delete("/{id}", status_code=200)
def eliminar_carrera_route(id: int) -> dict[str, str]:
    carrera = obtener_carrera_id(id)
    if not carrera:
        return {"mensaje": "Carrera no encontrada"}
    
    eliminar_carrera(carrera)  
    return {"mensaje": "Carrera eliminada"}

@router.put("/{id}", status_code=200)
def modificar_carrera_route(id : int, nueva_carrera : CarreraUpdate)-> dict: 
    carrera = obtener_carrera_id(id)
    if carrera:
        modificar_carrera(id, nueva_carrera)
        return {"mensaje": "Carrera modificada"}
    
    return {"mensaje": "Carrera NO encontrada"}    