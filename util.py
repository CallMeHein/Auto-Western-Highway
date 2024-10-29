import time
from threading import Thread
import system.lib.minescript as ms

from system.lib.minescript import EventQueue, EventType



def execute_command(command):
    while not stop_other_threads:
        command()
        time.sleep(1)


def wait_for_chat(text, command=None):
    # TODO LOG
    global stop_other_threads
    thread = None
    stop_other_threads = False
    with EventQueue() as event_queue:
        event_queue.register_chat_listener()
        if command:
            thread = Thread(target=execute_command, args=(command,))
            thread.start()
        while True:
            event = event_queue.get()
            if event.type == EventType.CHAT and text.lower() in event.message.lower():
                ms.echo("Got the message")
                stop_other_threads = True
                break
            if event.type == EventType.CHAT and "ok canceled" in event.message:
                return


def get_standing_block():
    player_position = [int(coord) for coord in ms.player_position()]
    player_position[0] -= 1
    player_position[1] -= 1
    player_position[2] = 0
    return player_position


def offset_block(block, x, y, z):
    return [block[0] + x, block[1] + y, block[2] + z]


def goto(position):
    ms.chat(f"#goto {position[0]} {position[1]} {position[2]}")
    time.sleep(0.25)
    wait_for_chat("No process in control", lambda: ms.chat("#proc"))
    ms.chat(f"#goto {position[0]} {position[1]} {position[2]}")
    time.sleep(0.25)
    wait_for_chat("No process in control", lambda: ms.chat("#proc"))
