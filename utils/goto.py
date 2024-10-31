import time
import system.lib.minescript as ms
from utils.get_player_position import get_player_position
from utils.wait_for_chat import wait_for_chat


def goto(position):
    """
    Move to the provided position using Baritone's goto function
    :param position: target [x, y, z]
    """
    # Baritone might overshoot and end up on a different coordinate than the target. Second iteration of the loop should almost always fix this.
    while get_player_position() != position:
        ms.echo(position)
        ms.echo(get_player_position())
        ms.chat(f"#goto {position[0]} {position[1]} {position[2]}")
        time.sleep(0.25)
        wait_for_chat("No process in control", lambda: ms.chat("#proc"))
        time.sleep(0.25)
