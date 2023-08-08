"""input/material/anisotropy.py

DESCRIPTION OF MATERIAL ANISOTROPY:
    - Link to manual/wiki
    - Papers

Raises:
    UniaxialAnisotropyOverloadedError: 
        raised if both options for setting material uniaxial anisotropy are specified

Returns:
    Anisotropy: material anisotropy input data model
"""


from enum import Enum
from pydantic import BaseModel, field_validator, FieldValidationInfo, FilePath
from pydantic.types import confloat
from .__errors import UniaxialAnisotropyOverloadedError


class UniaxialAnisotropyDirection(str, Enum):
    random = ("random",)
    random_grain = "random-grain"


class Anisotropy(BaseModel):
    """Anisotropy: material anisotropy input data model

    Raises:
        UniaxialAnisotropyOverloadedError: _description_

    Returns:
        _type_: _description_
    """

    # Unixaial anisotropy
    second_order_uniaxial_anisotropy_constant: confloat(
        ge=-1e-17, le=1e-17
    ) | None = None
    uniaxial_anisotropy_constant: confloat(ge=-1e-17, le=1e-17) | None = None
    fourth_order_uniaxial_anisotropy_constant: confloat(
        ge=-1e-17, le=1e-17
    ) | None = None

    # Triaxial anisotropy
    second_order_triaxial_anisotropy_vector: list[
        confloat(ge=-1e-10, le=1e-10)
    ] | None = None

    fourth_order_triaxial_anisotropy_vector: list[
        confloat(ge=-1e-10, le=1e-10)
    ] | None = None
    second_order_triaxial_basis_vector_1: list[float] | None = None
    second_order_triaxial_basis_vector_2: list[float] | None = None
    second_order_triaxial_basis_vector_3: list[float] | None = None
    fourth_order_triaxial_basis_vector_1: list[float] | None = None
    fourth_order_triaxial_basis_vector_2: list[float] | None = None
    fourth_order_triaxial_basis_vector_3: list[float] | None = None
    fourth_order_biaxial_anisotropy_constant: confloat(
        ge=-1e-17, le=1e-17
    ) | None = None
    sixth_order_uniaxial_anisotropy_constant: confloat(
        ge=-1e-17, le=1e-17
    ) | None = None
    fourth_order_cubic_anisotropy_constant: confloat(ge=-1e-17, le=1e-17) | None = None
    sixth_order_cubic_anisotropy_constant: confloat(ge=-1e-17, le=1e-17) | None = None
    neel_anisotropy_constant: confloat(ge=-1e-17, le=1e-17) | None = None
    lattice_anisotropy_constant: confloat(ge=-1e-17, le=1e-17) | None = None
    lattice_anisotropy_file: FilePath | None = None
    uniaxial_anisotropy_direction: UniaxialAnisotropyDirection | None

    cubic_anisotropy_direction_1: list[float] | None = None
    cubic_anisotropy_direction_2: list[float] | None = None
    fourth_order_rotational_anisotropy_constant: confloat(
        ge=-1e-17, le=1e-17
    ) | None = None

    @field_validator("uniaxial_anisotropy_constant")
    @classmethod
    def check_uniaxial_method(cls, uniaxial: float, info: FieldValidationInfo) -> float:
        if (
            uniaxial is not None
            and info.data["second_order_uniaxial_anisotropy_constant"] is not None
        ):
            raise UniaxialAnisotropyOverloadedError()
        return uniaxial
