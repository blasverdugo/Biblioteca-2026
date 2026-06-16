from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .carrera import Carrera
    from .prestamo import Prestamo

class Destinatario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=20)
    apellido: str = Field(max_length=20)
    dni: str = Field(index=True, unique=True)
    telefono: str = Field(max_length=15)
    correo: str = Field(max_length=20)

    id_carrera: int = Field(foreign_key="carrera.id")

    carrera: Optional["Carrera"] = Relationship(
    back_populates="destinatarios")

    prestamos: list["Prestamo"] = Relationship(
        back_populates="destinatario")



class DestinatarioCreate (SQLModel):
    nombre: str = Field(max_length=20)
    apellido: str = Field(max_length=20)
    dni: str = Field(index=True, unique=True)    
    telefono: str = Field(max_length=15)
    correo: str = Field(max_length=20)
    id_carrera: int = Field(foreign_key="carrera.id")

class DestinatarioGet(SQLModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    telefono: str
    correo: str
    id_carrera: int    

class DestinatarioUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, max_length=20)
    apellido: Optional[str] = Field(default=None, max_length=20)
    dni: Optional[str] = Field(default=None, index=True, unique=True)    
    telefono: Optional[str] = Field(default=None, max_length=15)
    correo: Optional[str] = Field(default=None, max_length=20)
    id_carrera: Optional[int] = Field(default=None, foreign_key="carrera.id")



