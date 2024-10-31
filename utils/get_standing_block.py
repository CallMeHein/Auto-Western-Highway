from types import XYZ
from utils.get_player_position import get_player_position


def get_standing_block() -> XYZ:
    """
    :return: [x, y, z] of the block the player is standing on
    """
    x, y, z = get_player_position()
    return [x, y - 1, z]
