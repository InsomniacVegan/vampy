from pydantic import BaseModel, FieldValidationInfo, field_validator
from pydantic.types import confloat, conint
from .__types import AtomOutputMethod, AtomOutputFormat, AtomOutputMode


class ConfigAtoms(BaseModel):
    atoms: AtomOutputMethod
    atoms_output_rate: conint(ge=0, le=1e6) = 1
    output_format: AtomOutputFormat
    output_mode: AtomOutputMode
    output_nodes: conint(ge=1, le=1e6)

    # Atom min/max
    atoms_minimum_x = confloat(ge=0.0, le=1.0)
    atoms_maximum_x = confloat(ge=0.0, le=1.0)
    atoms_minimum_y = confloat(ge=0.0, le=1.0)
    atoms_maximum_y = confloat(ge=0.0, le=1.0)
    atoms_minimum_z = confloat(ge=0.0, le=1.0)
    atoms_maximum_z = confloat(ge=0.0, le=1.0)


class ConfigMacroCells(BaseModel):
    macro_cells: AtomOutputMode
    macro_cells_output_rate: conint(ge=0, le=1e6) = 1


class ConfigSurfaceAtoms(BaseModel):
    identify_surface_atoms: bool = False


class ConfigField(BaseModel):
    field_range_descending_minimum: confloat(ge=-1e4, le=1e4)
    field_range_descending_maximum: confloat(ge=-1e4, le=1e4)

    field_range_ascending_minimum: confloat(ge=-1e4, le=1e4)
    field_range_ascending_maximum: confloat(ge=-1e4, le=1e4)


class Config(BaseModel):
    atoms: ConfigAtoms | None = None
    macro_cells: ConfigMacroCells | None = None
    surface_atoms: ConfigSurfaceAtoms | None = None
    field: ConfigField | None = None
