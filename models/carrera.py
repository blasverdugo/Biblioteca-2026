from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .destinatario import Destinatario


class Carrera(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50) 

    destinatarios: list["Destinatario"] = Relationship(
        back_populates="carrera"
    )

class CarreraCreate(SQLModel):
    nombre: str = Field(max_length=50)
    

class CarreraGet(SQLModel):
    id: int
    nombre: str
    

class CarreraUpdate(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: Optional[str] = Field(default=None, max_length=50)
    