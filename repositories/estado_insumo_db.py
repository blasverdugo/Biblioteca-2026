from sqlmodel import select 

from models.estado_insumo import EstadoInsumo,EstadoInsumoCreate, EstadoInsumoGet, EstadoInsumoUpdate 
from database.database import get_session

def crear_estado_insumo(estado_create: EstadoInsumoCreate) -> EstadoInsumo: 
    estado = EstadoInsumo.model_validate(estado_create)

    with get_session() as session:
        session.add(estado)
        session.commit()
        session.refresh(estado)
        return estado 
    
def obtener_todos_estado_insumos() -> list[EstadoInsumoGet]: 
    with get_session() as session: 
        statement = select(EstadoInsumo)
        return session.exec(statement).all() 
    


def obtener_estado_insumo_id(id: int) -> EstadoInsumo | None: 
    with get_session() as session:
        statement = select(EstadoInsumo).where(EstadoInsumo.id == id)
        return session.exec(statement).first()

def eliminar_estado_insumo(estado_insumo : EstadoInsumo) -> None:
    with get_session() as session:
        session.delete(estado_insumo)
        session.commit()
        

def modificar_estado_insumo(id: int, estado_actualizado: EstadoInsumoUpdate) -> EstadoInsumo | None:
    estado_insumo = obtener_estado_insumo_id(id)
    if not estado_insumo:
        return None

    # Convierte el objeto pydantic a diccionario, 
    # pero SOLO con los campos que llegaron en el request (ignora los None)
    datos = estado_actualizado.model_dump(exclude_unset=True)

    # Recorre cada campo y su valor
    for key, value in datos.items():
        # Le asigna el nuevo valor al objeto actual
        # es equivalente a hacer: estado_insumo.name = "nuevo nombre"
        setattr(estado_insumo, key, value)

    with get_session() as session:
        session.add(estado_insumo)
        session.commit()
        session.refresh(estado_insumo)
        return estado_insumo