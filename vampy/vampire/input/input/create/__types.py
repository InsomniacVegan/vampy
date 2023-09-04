from enum import Enum


class Creations(str, Enum):
    full = "full"
    cube = "cube"
    cylinder = "cylinder"
    ellipsoid = "ellipsoid"
    sphere = "sphere"
    truncated_octrahedron = "truncated-octrahedron"
    tear_drop = "tear-drop"
    particle = "particle"
    particle_array = "particle-array"
    hexagonal_particle_array = "hexagonal-particle-array"
    voronoi_film = "voronoi-film"


class xyz(str, Enum):
    x = "x"
    y = "y"
    z = "z"
