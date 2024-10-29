import time
from threading import Thread

import const
import system.lib.minescript as ms
from system.lib.minescript import EventQueue, EventType


def __execute_command(command, poll_rate):
    while not const.STOP_OTHER_THREADS:
        command()
        time.sleep(poll_rate)


def wait_for_chat(text, command=None, command_polling_rate=1.0):
    """
    Await a message containing a certain string in chat. Optionally execute a command while waiting.
    :param text: the message content to be awaited
    :param command: (optional) a function to be executed while waiting for the specified message
    :param command_polling_rate: (optional) amount of seconds to wait between execution of the provided command
    """
    const.STOP_OTHER_THREADS = False
    with EventQueue() as event_queue:
        event_queue.register_chat_listener()
        if command:
            thread = Thread(target=__execute_command, args=(command, command_polling_rate))
            thread.start()
        while True:
            event = event_queue.get()
            if event.type == EventType.CHAT and text.lower() in event.message.lower():
                const.STOP_OTHER_THREADS = True
                break
            if event.type == EventType.CHAT and "ok canceled" in event.message:
                const.STOP_OTHER_THREADS = True
                const.FULL_STOP = True
                return


def get_player_position():
    """
    :return: [x, y, z] of the player's feet
    """
    x, y, z = [int(coord) for coord in ms.player_position()]
    return [x - 1, y, z]


def get_standing_block():
    """
    :return: [x, y, z] of the block the player is standing on
    """
    x, y, z = get_player_position()
    return [x, y - 1, z]


def offset_block(block, x_off, y_off, z_off):
    """
    :return: [x, y, z] of block, offset by x_off, y_off, z_off
    """
    return [block[0] + x_off, block[1] + y_off, block[2] + z_off]


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
