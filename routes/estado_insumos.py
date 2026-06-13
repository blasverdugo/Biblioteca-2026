from fastapi import APIRouter
from models.estado_insumo import EstadoInsumo,EstadoInsumoRead, EstadoInsumoCreate, EstadoInsumoUpdate 
from repositories.estado_insumo_db import crear_estado_insumo, obtener_todos_estado_insumos, eliminar_estado_insumo, modificar_estado_insumo, obtener_estado_insumo_id



# routes/estado_insumos.py
router = APIRouter(prefix="/estado_insumos", tags=["Estado Insumos"])


@router.get("/", response_model=list[EstadoInsumoRead])
def obtener_estados_insumos():
    """ Obtiene una lista de todos los estados insumos disponibles en la base de datos.
    Returns:        list[EstadoInsumoRead]: Una lista de objetos que representan los estados insumos, cada uno con su ID, nombre y observación.
    """
    estado_insumos = obtener_todos_estado_insumos()
    
    return(estado_insumos)

@router.get("/{id}" , response_model=EstadoInsumoRead, status_code=200)
def obtener_estado_insumo_id_route(id:int):
    """ Obtiene un estado insumo por su ID.
    Args:        id (int): El ID del estado insumo a obtener.
    Returns:        EstadoInsumoRead: Un objeto que representa el estado insumo con el ID especificado, o None si no se encuentra."""


    estado = obtener_estado_insumo_id(id)
    return(estado)



@router.post("/", status_code=201, response_model=EstadoInsumoRead)
def agregar_estado_insumo_route(estado : EstadoInsumoCreate):
    """ Agrega un nuevo estado insumo a la base de datos.
    Args:        estado (EstadoInsumoCreate): Un objeto que contiene los datos del nuevo estado insumo a agregar.
    Returns:        EstadoInsumoRead: Un objeto que representa el estado insumo recién creado, incluyendo su ID asignado por la base de datos."""

    return crear_estado_insumo(estado)

@router.delete("/{id}", status_code=200)
def eliminar_estado_insumo_route(id : int) -> dict[str, str]:
    """ Elimina un estado insumo por su ID.
    Args:        id (int): El ID del estado insumo a eliminar.
    Returns:        dict[str, str]: Un diccionario con un mensaje indicando el resultado de la operación."""


    estado = obtener_estado_insumo_id(id)
    if estado:
        eliminar_estado_insumo(id)
        return {"mensaje": "Estado insumo eliminado"}
    
    return {"mensaje": "Estado insumo NO encontrado"}



@router.put("/{id}", status_code=200)
def modificar_estado_insumo_route(id : int, nuevo_estado : EstadoInsumoUpdate)-> dict: 
    """ Modifica un estado insumo existente.
    Args:        id (int): El ID del estado insumo a modificar.
        nuevo_estado (EstadoInsumoUpdate): Un objeto que contiene los nuevos datos del estado insumo.
    Returns:        dict: Un diccionario con un mensaje indicando el resultado de la operación."""



    estado_viejo = obtener_estado_insumo_id(id) 
    if estado_viejo :
        modificar_estado_insumo(id, nuevo_estado)
        return {"mensaje": "Estado insumo modificado"}
    return {"mensaje": "NO encontrado"}