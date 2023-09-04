from enum import Enum


class AtomOutputMethod(str, Enum):
    continuous = "continuous"
    end = "end"


class AtomOutputFormat(str, Enum):
    binary = "binary"
    text = "text"


class AtomOutputMode(str, Enum):
    legacy = "legacy"
    mpi_io = "mpi-io"
    file_per_process = "file-per-process"
    file_per_node = "file-per-node"
