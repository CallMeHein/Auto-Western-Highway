import copy
import const
import system.lib.minescript as ms
from annotations import XYZ
from const import STEP_HEIGHT_MIN
from down import get_step_down_height, downward_scaffold, step_down
from settings import setup_settings
from up import get_step_up_height, upward_scaffold, step_up
from utils.get_player_position import get_player_position
from utils.get_standing_block import get_standing_block
from utils.goto import goto
from utils.offset_block import offset_block
from utils.wait_for_chat import wait_for_chat

# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)


def step(standing_block: XYZ) -> None:
    ms.chat("#build step.litematic ~-1 ~-1 -1")
    wait_for_chat("Done building")
    goto(offset_block(standing_block, -1, 1, 0))


def auto_highway() -> None:
    setup_settings()
    x, y, z = get_player_position()
    goto([x, y, 0])
    while not const.FULL_STOP:
        standing_block = get_standing_block()
        step_up_height = get_step_up_height(standing_block)
        if step_up_height >= STEP_HEIGHT_MIN:
            upward_scaffold(step_up_height)
            goto(offset_block(standing_block, 0, 1, 0))
            step_up(step_up_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_up_height, step_up_height + 1, 0))
            continue
        step_down_height = get_step_down_height(standing_block)
        if step_down_height >= STEP_HEIGHT_MIN:
            downward_scaffold(step_down_height)
            goto(offset_block(standing_block, 0, 1, 0))
            step_down(step_down_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_down_height, -step_down_height + 1, 0))
            continue
        step(standing_block)


if __name__ == "__main__":
    auto_highway()
