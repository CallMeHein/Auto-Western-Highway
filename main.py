import copy
import pydevd_pycharm
import const
import system.lib.minescript as ms
from const import STEP_HEIGHT_MIN
from down import should_step_down, downward_scaffold, step_down
from settings import setup_settings
from up import should_step_up, upward_scaffold, step_up
from util import wait_for_chat, get_standing_block, offset_block, goto, get_player_position


# pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)


def step(standing_block, below=False, move_after=True):
    if below:
        ms.chat("#build step.litematic ~ ~-1 -1")
    else:
        ms.chat("#build step.litematic ~-1 ~-1 -1")
    wait_for_chat("Done building")
    if move_after:
        goto(offset_block(standing_block, -1, 1, 0))


def auto_highway():
    setup_settings()
    x, y, z = get_player_position()
    goto([x, y, 0])
    while not const.FULL_STOP:
        standing_block = get_standing_block()
        step_up_height = should_step_up(standing_block)
        if step_up_height >= STEP_HEIGHT_MIN:
            upward_scaffold(step_up_height)
            goto(offset_block(standing_block, 0, 1, 0))
            step_up(step_up_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_up_height, step_up_height + 1, 0))
            continue
        step_down_height = should_step_down(standing_block)
        if step_down_height >= STEP_HEIGHT_MIN:
            downward_scaffold(step_down_height)
            goto(offset_block(standing_block, 0, 1, 0))
            step_down(step_down_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_down_height, -step_down_height + 1, 0))
            continue
        step(standing_block)


if __name__ == "__main__":
    auto_highway()
