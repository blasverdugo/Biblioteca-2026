from sqlmodel import select 

from models.carrera import Carrera,CarreraCreate, CarreraGet, CarreraUpdate 
from database.database import get_session

def crear_carrera(carrera_create: CarreraCreate) -> Carrera: 
    carrera = Carrera.model_validate(carrera_create)

    with get_session() as session:
        session.add(carrera)
        session.commit()
        session.refresh(carrera)
        return carrera

def   obtener_todas_las_carreras() -> list[CarreraGet]: 
    with get_session() as session: 
        statement = select(Carrera)
        return session.exec(statement).all()

def obtener_carreras_id(id: int) -> Carrera | None: 
    with get_session() as session:
        statement = select(Carrera).where(Carrera.id == id)
        return session.exec(statement).first()

def eliminar_carrera(carrera : Carrera) -> None:
    with get_session() as session:
        session.delete(carrera)
        session.commit()
        
    
def modificar_carrera(id: int, carrera_actualizada: CarreraUpdate) -> Carrera | None:
    carrera = obtener_carreras_id(id)
    if not carrera:
        return None

    datos = carrera_actualizada.model_dump(exclude_unset=True)
    for key, value in datos.items():
        setattr(carrera, key, value)

    with get_session() as session:
        session.add(carrera)
        session.commit()
        session.refresh(carrera)
        return carrera    