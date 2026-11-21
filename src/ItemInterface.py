from dataclasses import dataclass
from typing import NewType


@dataclass
class Item:
    capacidade: int
    alerta: str
