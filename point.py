from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Point:
    value: Optional[int] = None
    left: bool = False
    top: bool = False
    right: bool = False
    bottom: bool = False

    def __repr__(self) -> str:
        borders = ""
        if self.left:
            borders += "L"
        if self.top:
            borders += "T"
        if self.right:
            borders += "R"
        if self.bottom:
            borders += "B"
        return f"Point({self.value} [{borders}])"
