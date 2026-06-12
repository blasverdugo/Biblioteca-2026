from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from .prestamo import Prestamo


class EstadoInsumo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=20)
    observacion: str = Field(max_length=50)

    insumos: list["Insumo"] = Relationship(
        back_populates="estado"
    )


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