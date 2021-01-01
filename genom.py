from dataclasses import dataclass


@dataclass
class GenomFixed:
    energy: float = 12
    div_energy: float = 69
    cell_type: int = 0
    inp_energy: float = 2
    energy2live: float = 0.1


@dataclass
class GenomMovable(GenomFixed):
    velocity: float = 1.0
    energy2move: int = 0.01

