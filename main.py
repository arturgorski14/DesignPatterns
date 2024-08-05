# This is a sample Python script.
import logging

from builder_pattern import Director, VersatileHouseBuilder, House

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.  # noqa E501

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def builder_pattern_simple():
    wood_builder = VersatileHouseBuilder("wooden")
    director = Director()
    director.set_builder(wood_builder)

    house = director.build_simple_house()
    print(house)


def builder_pattern() -> House:
    """
    Construct a house based on the client's specifications:
    - 10 stone walls
    - 2 wooden doors and 1 stone door
    - 4 wooden windows and 4 glass windows
    - Tiled roof
    - Metal garage
    The order of construction is important and followed as specified.

    :return: Constructed House object
    """
    # Initialize builders with their respective materials
    stone_builder = VersatileHouseBuilder("stone")
    wood_builder = VersatileHouseBuilder("wooden")
    glass_builder = VersatileHouseBuilder("glass")
    tile_builder = VersatileHouseBuilder("tile")
    metal_builder = VersatileHouseBuilder("metal")

    # Build the house with stone walls
    house = stone_builder.build_walls(10)

    # Build doors: 2 wooden doors, followed by 1 stone door
    house = wood_builder.build_doors(2, house)
    house = stone_builder.build_doors(1, house)

    # Build windows: 4 wooden windows, followed by 4 glass windows
    house = wood_builder.build_windows(4, house)
    house = glass_builder.build_windows(4, house)

    # Build roof: tiled roof
    house = tile_builder.build_roof(house)

    # Build garage: metal garage
    house = metal_builder.build_garage(house)

    # Print the final house
    print(house)

    # Return the constructed house for further use or validation
    return house


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    builder_pattern()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
