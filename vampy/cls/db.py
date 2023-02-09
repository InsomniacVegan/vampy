"""DOCSTRING"""
from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Experiment:
    """Experiment block"""

    id    : str = field(default_factory=uuid4)
    label : str
    runs  : list
    notes : str


@dataclass
class Run:
    """Run block"""

    id          : str = field(default_factory=uuid4)
    label       : str
    system      : str
    simulation  : str
    environment : str
    notes       : str


@dataclass
class Environment:
    """Environment block"""

    id          : str = field(default_factory=uuid4)
    label       : str
    object      : str #path
    object_type : str
    notes       : str


@dataclass
class System:
    """System block"""

    id     : str = field(default_factory=uuid4)
    label  : str
    object : str # Refactor to system object


@dataclass
class Simulation:
    """Simulation block"""

    id     : str = field(default_factory=uuid4)
    label  : str
    object : str # Refactor to sim object


@dataclass
class Data:
    """Data block"""

    id    : str = field(default_factory=uuid4)
    label : str = field(default=None)
    data  : str # Path