from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship



if TYPE_CHECKING:
    from .insumo import Insumo

class EstadoInsumo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=20)
    observacion: str = Field(max_length=50)

    insumos: list["Insumo"] = Relationship(
        back_populates="estado"
    )


    def nombre_completo(self) -> str:
        return f"{self.nombre}"