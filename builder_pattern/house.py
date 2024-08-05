from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class House:
    walls: List[str] = field(default_factory=list)
    doors: List[str] = field(default_factory=list)
    windows: List[str] = field(default_factory=list)
    roof: str = ""
    garage: Optional[str] = None

    def __str__(self) -> str:
        garage_info = f"- Garage: {self.garage}" if self.garage else "- No Garage"
        return (
            f"House:\n"
            f"- Walls: {len(self.walls)} ({', '.join(self.walls)})\n"
            f"- Doors: {len(self.doors)} ({', '.join(self.doors)})\n"
            f"- Windows: {len(self.windows)} ({', '.join(self.windows)})\n"
            f"- Roof: {self.roof}\n"
            f"{garage_info}\n"
        )
