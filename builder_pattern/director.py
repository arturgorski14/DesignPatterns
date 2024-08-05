from typing import Optional

from .builders import HouseBuilder
from .house import House


class Director:
    """Director class to construct houses using different builders."""

    def __init__(self) -> None:
        self.builder: Optional[HouseBuilder] = None

    def set_builder(self, builder: HouseBuilder) -> None:
        """Assigns a builder_pattern to the director."""
        self.builder = builder

    def build_simple_house(self) -> House:
        """Builds a simple house with minimal elements."""
        if not self.builder:
            raise ValueError("Builder not set.")

        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        return self.builder.get_result()

    def build_custom_house(
        self,
        walls: int,
        doors: int,
        windows: int,
        with_roof: bool = True,
        with_garage: bool = True,
    ) -> House:
        """Builds a house with custom parameters."""
        if not self.builder:
            raise ValueError("Builder not set.")

        self.builder.reset()
        self.builder.build_walls(num=walls)
        self.builder.build_doors(num=doors)
        self.builder.build_windows(num=windows)
        if with_roof:
            self.builder.build_roof()
        if with_garage:
            self.builder.build_garage()
        return self.builder.get_result()
