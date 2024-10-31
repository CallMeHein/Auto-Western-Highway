import system.lib.minescript as ms


def get_player_position():
    """
    :return: [x, y, z] of the player's feet
    """
    x, y, z = [int(coord) for coord in ms.player_position()]
    return [x - 1, y, z]
