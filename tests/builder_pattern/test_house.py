from builder_pattern.house import House


def test_house_initialization():
    """Test the default initialization of House."""
    house = House()
    assert house.walls == []
    assert house.doors == []
    assert house.windows == []
    assert house.roof == ""
    assert house.garage is None


def test_house_initialization_with_values():
    """Test the initialization of House with custom values."""
    walls = ["wooden", "stone"]
    doors = ["wooden"]
    windows = ["glass"]
    roof = "tile"
    garage = "metal"

    house = House(walls=walls, doors=doors, windows=windows, roof=roof, garage=garage)

    assert house.walls == walls
    assert house.doors == doors
    assert house.windows == windows
    assert house.roof == roof
    assert house.garage == garage


def test_house_str_method():
    """Test the string representation of House."""
    house = House(
        walls=["wooden", "stone"],
        doors=["wooden"],
        windows=["glass"],
        roof="tile",
        garage="metal",
    )
    expected_str = (
        "House:\n"
        "- Walls: 2 (wooden, stone)\n"
        "- Doors: 1 (wooden)\n"
        "- Windows: 1 (glass)\n"
        "- Roof: tile\n"
        "- Garage: metal\n"
    )
    assert str(house) == expected_str


def test_house_str_method_no_garage():
    """Test the string representation of House when no garage."""
    house = House(
        walls=["wooden", "stone"], doors=["wooden"], windows=["glass"], roof="tile"
    )
    expected_str = (
        "House:\n"
        "- Walls: 2 (wooden, stone)\n"
        "- Doors: 1 (wooden)\n"
        "- Windows: 1 (glass)\n"
        "- Roof: tile\n"
        "- No Garage\n"
    )
    assert str(house) == expected_str
