from sqlmodel import select 

from models.destinatario import Destinatario,DestinatarioCreate, DestinatarioGet, DestinatarioUpdate 
from database.database import get_session

def crear_destinatario(destinatario_create: DestinatarioCreate) -> Destinatario: 
    destinatario = Destinatario.model_validate(destinatario_create)

    with get_session() as session:
        session.add(destinatario)
        session.commit()
        session.refresh(destinatario)
        return destinatario
    

def obtener_destinatario_por_dni(dni: str) -> Destinatario | None:
    with get_session() as session:
        statement = select(Destinatario).where(Destinatario.dni == dni)
        return session.exec(statement).first()


def   obtener_todos_destinatarios() -> list[DestinatarioGet]: 
    with get_session() as session: 
        statement = select(Destinatario)
        return session.exec(statement).all()

def obtener_destinatario_id(id: int) -> Destinatario | None: 
    with get_session() as session:
        statement = select(Destinatario).where(Destinatario.id == id)
        return session.exec(statement).first()

def eliminar_destinatario(destinatario : Destinatario) -> None:
    with get_session() as session:
        session.delete(destinatario)
        session.commit()
           
    
def modificar_destinatario(id: int, destinatario_actualizado: DestinatarioUpdate) -> Destinatario | None:
    destinatario = obtener_destinatario_id(id)
    if not destinatario:
        return None

    datos = destinatario_actualizado.model_dump(exclude_unset=True)
    for key, value in datos.items():
        setattr(destinatario, key, value)

    with get_session() as session:
        session.add(destinatario)
        session.commit()
        session.refresh(destinatario)
        return destinatario    