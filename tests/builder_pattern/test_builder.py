import logging

import pytest

from builder_pattern import VersatileHouseBuilder


@pytest.fixture
def wood_builder():
    """Fixture for creating a fresh VersatileHouseBuilder instance."""
    return VersatileHouseBuilder("wooden")


@pytest.fixture
def stone_builder():
    """Fixture for creating a fresh StoneHouseBuilder instance."""
    return VersatileHouseBuilder("stone")


@pytest.fixture
def house_builder(request):
    """Fixture that provides different builders based on the request."""
    if request.param == "wood":
        return VersatileHouseBuilder("wooden")
    elif request.param == "stone":
        return VersatileHouseBuilder("stone")
    else:
        raise ValueError("Unknown builder type")


def test_initial_state(wood_builder, caplog):
    """Test that the builder starts with an empty house and no logs."""
    with caplog.at_level(logging.DEBUG):
        house = wood_builder.get_result()
        assert house.walls == []
        assert house.doors == []
        assert house.windows == []
        assert house.roof == ""
        assert house.garage is None
        assert len(caplog.records) == 0  # No logs should be generated


def test_reset(wood_builder, caplog):
    """Test resetting the builder and verify logging."""
    with caplog.at_level(logging.DEBUG):
        wood_builder.build_walls(4)
        wood_builder.reset()
        house = wood_builder.get_result()
        assert house.walls == []
        assert house.doors == []
        assert house.windows == []
        assert house.roof == ""
        assert house.garage is None
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "DEBUG"
        assert "Built 4 wooden walls" in caplog.records[0].message


@pytest.mark.parametrize("house_builder", ["wood", "stone"], indirect=True)
def test_build_custom_house(house_builder, caplog):
    """Test building a house with custom parameters and verify logging."""
    with caplog.at_level(logging.DEBUG):
        house_builder.build_walls(num=5)
        house_builder.build_doors(num=2)
        house_builder.build_windows(num=4)
        house_builder.build_roof()
        house_builder.build_garage()

        house = house_builder.get_result()
        assert len(house.walls) == 5
        assert len(house.doors) == 2
        assert len(house.windows) == 4
        assert house.roof == f"{house_builder.material} roof"
        assert house.garage == f"{house_builder.material} garage"

        assert len(caplog.records) == 5
        assert f"Built 5 {house_builder.material} walls" in caplog.records[0].message
        assert f"Built 2 {house_builder.material} doors" in caplog.records[1].message
        assert f"Built 4 {house_builder.material} windows" in caplog.records[2].message
        assert f"Built a {house_builder.material} roof" in caplog.records[3].message
        assert f"Built a {house_builder.material} garage" in caplog.records[4].message


def test_invalid_wall_count(wood_builder, caplog):
    """Test building walls with an invalid count and verify logging."""
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ValueError, match="Number of items must be at least 1"):
            wood_builder.build_walls(0)
        assert len(caplog.records) == 0  # No successful log should be generated


def test_invalid_window_count(wood_builder, caplog):
    """Test building windows with an invalid count and verify logging."""
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ValueError, match="Number of items must be at least 1"):
            wood_builder.build_windows(0)
        assert len(caplog.records) == 0  # No successful log should be generated


def test_invalid_door_count(wood_builder, caplog):
    """Test building doors with an invalid count and verify logging."""
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(ValueError, match="Number of items must be at least 1"):
            wood_builder.build_doors(0)
        assert len(caplog.records) == 0  # No successful log should be generated
