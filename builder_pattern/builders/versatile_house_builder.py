import logging
from typing import List, Optional

from builder_pattern.house import House

from .house_builder import HouseBuilder

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VersatileHouseBuilder(HouseBuilder):
    """Concrete builder that creates houses with specified material."""

    def __init__(self, material: str) -> None:
        self.material = material
        self.house: House = House()

    def reset(self) -> None:
        """Resets the builder to start fresh."""
        self.house = House()

    def build_walls(self, num: int = 4, house: Optional[House] = None) -> House:
        house = house or self.house
        house.walls += self._build_x_times(num)
        self._log_building("wall", num, house)
        return house

    def build_doors(self, num: int = 1, house: Optional[House] = None) -> House:
        house = house or self.house
        house.doors += self._build_x_times(num)
        self._log_building("door", num, house)
        return house

    def build_windows(self, num: int = 3, house: Optional[House] = None) -> House:
        house = house or self.house
        house.windows += self._build_x_times(num)
        self._log_building("window", num, house)
        return house

    def build_roof(self, house: Optional[House] = None) -> House:
        house = house or self.house
        house.roof = f"{self.material} roof"
        logger.debug(f"Built a {self.house.roof}.")
        return house

    def build_garage(self, house: Optional[House] = None) -> House:
        house = house or self.house
        house.garage = f"{self.material} garage"
        logger.debug(f"Built a {self.house.garage}.")
        return house

    def get_result(self) -> House:
        return self.house

    def _build_x_times(self, num: int) -> List[str]:
        """Helper method to create a list of material items."""
        if num < 1:
            raise ValueError("Number of items must be at least 1.")
        return [self.material for _ in range(num)]

    def _log_building(self, item: str, num: int, house: House) -> None:
        """Helper method to log the building process."""
        logger.debug(
            f"Built {num} {self.material} {item}{'s' if num > 1 else ''} in {'existing' if house is not self.house else 'new'} house."  # noqa E501
        )
