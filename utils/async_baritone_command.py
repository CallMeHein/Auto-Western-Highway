import time
from threading import Thread

import system.lib.minescript as ms


def __execute_command(command: str, delay: float) -> None:
    time.sleep(delay)
    ms.chat(command)


def async_baritone_command(command: str, delay: float = 0.25) -> None:
    thread = Thread(target=__execute_command, args=(command, delay))
    thread.start()
