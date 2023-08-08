from enum import Enum
from typing import Sequence
from pydantic import BaseModel, FieldValidationInfo, field_validator
from pydantic.types import confloat
from .__errors import MacroCellSizeOverloaded


class AtomOutputMethod(str, Enum):
    continuous = ("continuous",)
    end = "end"


class ConfigAtoms(BaseModel):
    atoms: AtomOutputMethod
    atoms_output_rate: int = 1


class Config(BaseModel):
    # Specify
    # macro_cell_size: confloat(ge=0, le=1e7) | Sequence[confloat(ge=0, le=1e7)]

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

    @field_validator("macro_cell_size_x", "macro_cell_size_y", "macro_cell_size_z")
    @classmethod
    def check_macro_dims(cls, dim: float, info: FieldValidationInfo) -> float:
        if info.date["macro_cell_size"] is None and dim is None:
            raise MacroCellDimensionNotSpecified("")
        cell_dimensions = {
            "x": info.data["macro_cell_size_x"],
            "y": info.data["macro_cell_size_y"],
            "z": info.data["macro_cell_szie_z"],
        }

        empty_dims = {dim for dim, size in cell_dimensions.items() if size is None}

        print(len(empty_dims))

        # if macro_cell_size is None and None in (
        #     info.data["macro_cell_size_x"],
        #     info.data["macro_cell_size_y"],
        #     info.data["macro_cell_szie_z"]
        # ):

        # raise MacroCellSizeDimensionNotSpecified()
