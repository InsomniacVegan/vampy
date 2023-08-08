from pydantic import BaseModel, FieldValidationInfo, field_validator
from pydantic.types import confloat
from .__errors import SurfaceAnisotropyThresholdOverloadedError


class Anisotropy(BaseModel):
    # Currently surface-anisotropy-threshold is overloaded
    # Suggest refactor to two commands:
    #  surface-anisotropy-threshold
    #  surface-anisotropy-threshold-native

    surface_anisotropy_threshold: str | int | None = None
    surface_anisotropy_threshold_native: bool | None = None

    surface_anisotropy_nearest_neighbour_range: confloat(ge=0, le=1e9) | None = None
    enable_bulk_neel_anisotropy: bool | None = None
    neel_anisotropy_exponential_factor: confloat(ge=0.1, le=100) | None = None
    neel_anisotropy_exponential_range: confloat(gt=0, le=1000) | None = None

    # Validation
    @field_validator("surface_anisotropy_threshold_native")
    @classmethod
    def check_threshold_single(cls, native: bool, info: FieldValidationInfo) -> bool:
        if native and info["surface_anisotropy_threshold"] is not None:
            print("Surface anisotropy threshold overloaded")
            print(
                "Specify only one of [surface_anisotropy_threshold, surface_anisotropy_threshold_native]"
            )
            raise SurfaceAnisotropyThresholdOverloadedError(
                "Surface anisotropy threshold overloaded"
            )
        return native
