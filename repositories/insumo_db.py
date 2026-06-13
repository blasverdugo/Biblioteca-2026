from sqlmodel import select 

from models.insumo import Insumo 
from database.database import get_session

#crear_insumo, obtener_todos_insumos, eliminar_insumo, modificar_insumo, obtener_insumo_id

def crear_insumo(insumo: Insumo): 
    with get_session() as session:
        session.add(insumo)
        session.commit()
        session.refresh(insumo)
        return insumo 
    
def obtener_todos_insumos(): 
    with get_session() as session: 
        statement = select(Insumo)
        return session.exec(statement).all() 
    
def obtener_insumo_id(id: int): 
    with get_session() as session:
        statement = select(Insumo).where(Insumo.id == id)
        return session.exec(statement).first()

def eliminar_insumo(id: int):
    insumo = obtener_insumo_id(id)
    with get_session() as session:
        session.delete(insumo)
        session.commit()
        session.refresh(insumo)
        return {"ok": True} 

def modificar_insumo(id, ins): 
     insumo = obtener_insumo_id(id)
     with get_session() as session:
         session.add() 