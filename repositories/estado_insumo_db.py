from sqlmodel import select 

from models.estado_insumo import EstadoInsumo,EstadoInsumoCreate, EstadoInsumoRead, EstadoInsumoUpdate 
from database.database import get_session

def crear_estado_insumo(estado_create: EstadoInsumoCreate) -> EstadoInsumo: 
    estado = EstadoInsumo.model_validate(estado_create)

    with get_session() as session:
        session.add(estado)
        session.commit()
        session.refresh(estado)
        return estado 
    
def obtener_todos_estado_insumos() -> list[EstadoInsumoRead]: 
    with get_session() as session: 
        statement = select(EstadoInsumo)
        return session.exec(statement).all() 
    


def obtener_estado_insumo_id(id: int) -> EstadoInsumo | None: 
    with get_session() as session:
        statement = select(EstadoInsumo).where(EstadoInsumo.id == id)
        return session.exec(statement).first()

def eliminar_estado_insumo(id: int) -> dict[str, bool]:
    estado_insumo = obtener_estado_insumo_id(id)
    with get_session() as session:
        session.delete(estado_insumo)
        session.commit()
        session.refresh(estado_insumo)
        return {"ok": True} 

def modificar_estado_insumo(id: int, estado_actualizado: EstadoInsumoUpdate) -> EstadoInsumo | None:
    estado_insumo = obtener_estado_insumo_id(id)
    if not estado_insumo:
        return None


    datos = estado_actualizado.model_dump(exclude_unset=True)
    for key, value in datos.items():
        setattr(estado_insumo, key, value)

    with get_session() as session:
        session.add(estado_insumo)
        session.commit()
        session.refresh(estado_insumo)
        return estado_insumo