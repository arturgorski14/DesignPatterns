from typing import Optional, Protocol

from builder_pattern.house import House


class HouseBuilder(Protocol):
    """Interface for house builder classes."""

    def reset(self) -> None:
        raise NotImplementedError

    def build_walls(self, num: int = 4, house: Optional[House] = None) -> House:
        raise NotImplementedError

    def build_doors(self, num: int = 1, house: Optional[House] = None) -> House:
        raise NotImplementedError

    def build_windows(self, num: int = 3, house: Optional[House] = None) -> House:
        raise NotImplementedError

    def build_roof(self, house: Optional[House] = None) -> House:
        raise NotImplementedError

    def build_garage(self, house: Optional[House] = None) -> House:
        raise NotImplementedError

    def get_result(self) -> House:
        raise NotImplementedError
