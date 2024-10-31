import time
from threading import Thread
from typing import Callable

import const
from system.lib.minescript import EventQueue, EventType


def __execute_command(command: Callable, poll_rate: float) -> None:
    while not const.STOP_OTHER_THREADS:
        command()
        time.sleep(poll_rate)


def wait_for_chat(text: str, command: Callable = None, command_polling_rate: float = 1.0) -> None:
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
