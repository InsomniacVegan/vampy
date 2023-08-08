from typing import Sequence
from pydantic import BaseModel, FieldValidationInfo, field_validator, model_validator
from pydantic.types import confloat
from __errors import MacroCellSizeOverloaded, MacroCellDimensionNotSpecified


class MacroCell(BaseModel):
    # Proposed change to single variable import
    macro_cell_size_new: confloat(ge=0, le=1e7) | Sequence[confloat(ge=0, le=1e7)]

    macro_cell_size_x: confloat(ge=0, le=1e7) | None = None
    macro_cell_size_y: confloat(ge=0, le=1e7) | None = None
    macro_cell_size_z: confloat(ge=0, le=1e7) | None = None
    macro_cell_size: confloat(ge=0, le=1e7) | None = None

    @field_validator("macro_cell_size")
    @classmethod
    def limit_cell_or_dimensions(
        cls, macro_cell_size: float, info: FieldValidationInfo
    ) -> float:
        if macro_cell_size and info.data["macro_cell_size_x"]:
            raise MacroCellSizeOverloaded
        return macro_cell_size

    @model_validator(mode="after")
    @classmethod
    def check_macro_dims(self) -> "MacroCell":
        if self.macro_cell_size is None and None in [
            self.macro_cell_size_x,
            self.macro_cell_size_y,
            self.macro_cell_size_z,
        ]:
            raise MacroCellDimensionNotSpecified()


cell_dims = {
    "macro_cell_size_x": 20,
    "macro_cell_size_y": 20,
    "macro_cell_size_z": 20,
}

cell = MacroCell(**cell_dims)
