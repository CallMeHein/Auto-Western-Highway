import system.lib.minescript as ms
from annotations import XYZ


def get_player_position() -> XYZ:
    """
    :return: [x, y, z] of the player's feet
    """
    x, y, z = [int(coord) for coord in ms.player_position()]
    return [x - 1, y, z]
