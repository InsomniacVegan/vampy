from typing import Sequence
from pydantic import BaseModel, FieldValidationInfo, field_validator, model_validator
from pydantic.types import confloat, conint
from .__errors import FacetedParticleUndefined, VoronoiNotSelected
from .__types import Creations, xyz


class CreateFacetedParticle(BaseModel):
    faceted_particle: Sequence(conint(ge=1, le=1000))

    @field_validator("faceted_particle")
    @classmethod
    def faceted_particle_len(
        cls, facted_particle: Sequence[int], info: FieldValidationInfo
    ) -> Sequence[int]:
        if len(facted_particle) != 3:
            raise FacetedParticleUndefined(len(facted_particle))
        else:
            return facted_particle


class Voronoi(BaseModel):
    grain_substructure: bool = False
    size_variance: confloat(ge=0.0, le=1.0) | None = None
    row_offset: bool = False
    random_seed: conint(ge=0, le=2e9) | None = None
    rounded_grains: bool = False
    include_boundary_grains: bool = False
    rounded_grains_area: confloat(ge=0.0, le=1.0)


class PeriodicBoundaries(BaseModel):
    periodic_boundaries: bool = False
    period_boundaries


class Create(BaseModel):
    creation: Creations | None = None
    facted_particle: CreateFacetedParticle | None = None
    voronoi: Voronoi | None = None
    particle_centre_offset: bool = False
    single_spin: bool = False
    periodic_boundaires: PeriodicBoundaries | None = None

    @field_validator("voronoi")
    @classmethod
    def voronoi_creation(cls, voronoi: Voronoi, info: FieldValidationInfo) -> Voronoi:
        if voronoi and info.data["creation"] != "voronoi-film":
            raise VoronoiNotSelected
        return voronoi
