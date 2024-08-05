from unittest.mock import Mock

import pytest

from builder_pattern import HouseBuilder
from builder_pattern.director import Director
from builder_pattern.house import House


@pytest.fixture
def director():
    return Director()


@pytest.fixture
def mock_builder():
    mock = Mock(spec=HouseBuilder)
    mock.get_result.return_value = House()
    return mock


def test_build_default_simple_house(director, mock_builder):
    director.set_builder(mock_builder)

    director.build_simple_house()

    mock_builder.reset.assert_called_once()
    mock_builder.build_walls.assert_called_once_with()
    mock_builder.build_doors.assert_called_once_with()
    mock_builder.build_windows.assert_called_once_with()
    mock_builder.build_roof.assert_called_once_with()
    mock_builder.build_garage.assert_not_called()

    mock_builder.get_result.assert_called_once()
    house = mock_builder.get_result()
    assert isinstance(house, House)


def test_build_custom_wood_house(mock_builder):
    """Test building a wood house with custom parameters."""
    director = Director()
    director.set_builder(mock_builder)

    director.build_custom_house(walls=5, doors=2, windows=4)

    mock_builder.build_walls.assert_called_once_with(num=5)
    mock_builder.build_doors.assert_called_once_with(num=2)
    mock_builder.build_windows.assert_called_once_with(num=4)
    mock_builder.build_roof.assert_called_once()
    mock_builder.build_garage.assert_called_once()

    mock_builder.get_result.assert_called_once()


def test_build_custom_stone_house(mock_builder):
    """Test building a stone house with custom parameters."""
    director = Director()
    director.set_builder(mock_builder)

    director.build_custom_house(walls=10, doors=3, windows=8)

    mock_builder.build_walls.assert_called_once_with(num=10)
    mock_builder.build_doors.assert_called_once_with(num=3)
    mock_builder.build_windows.assert_called_once_with(num=8)
    mock_builder.build_roof.assert_called_once()
    mock_builder.build_garage.assert_called_once()

    mock_builder.get_result.assert_called_once()
