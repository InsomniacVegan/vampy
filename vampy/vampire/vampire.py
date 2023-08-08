"""DOCTSRING"""
from dataclasses import dataclass


@dataclass
class VParam:
    """Unit building block of VAMPIRE inputs"""

    label: str
    value: str = False
    unit: str = False
    type: str = "__vparam__"


@dataclass
class VBlock:
    """Collection object for parameters for use with VAMPIRE"""

    label: str
    params: list[VParam]
    type: str = "__vblock__"


@dataclass
class VInput:
    """Overall container for VAMPIRE input file"""

    label: str
    blocks: list[VBlock]
    type: str = "__vinput__"


@dataclass
class VMaterialBlock:
    """Material container"""

    id: int
    params: list[VParam]
    type: str = "__vmaterialblock__"


@dataclass
class VMaterial:
    """Material file controller"""

    materials: list[VMaterialBlock]
    type: str = "__vmaterial__"
