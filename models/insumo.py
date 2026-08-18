from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .prestamo import Prestamo
    from .estado_insumo import EstadoInsumo



class Insumo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    codigo: str = Field(unique=True, max_length=10, index=True)
    nombre: str = Field(max_length=50)
    ubicacion: str = Field(max_length=50)

    id_estado: int = Field(foreign_key="estadoinsumo.id")

    estado: Optional["EstadoInsumo"] = Relationship(
        back_populates="insumos"
    )

    prestamos: list["Prestamo"] = Relationship(
        back_populates="insumo"
    )

    def nombre_completo(self) -> str:
        return f"{self.codigo} {self.nombre}"

class InsumoUpdate(SQLModel): #---> Sirve para actualizar parcialmente un insumo, sin enviar tdos los campos
    id: int | None = None 
    codigo: str  | None = None
    nombre: str | None = None
    ubicacion: str  | None = None
    id_estado: int | None = None