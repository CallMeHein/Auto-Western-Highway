import copy
import const
from const import STEP_HEIGHT_MIN
from down import get_step_down_height, downward_scaffold, step_down, get_future_step_down_length
from utils.reset_settings import reset_settings
from type_annotations import XYZ
from up import get_step_up_height, upward_scaffold, step_up, get_future_step_up_length
from utils.baritone_build import baritone_build
from utils.get_player_position import get_player_position
from utils.get_standing_block import get_standing_block
from utils.goto import goto
from utils.offset_block import offset_block

# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)


def step(starting_block: XYZ, count=1) -> None:
    starting_block = offset_block(starting_block, 0, 1, 0)
    for _ in range(count):
        goto(starting_block)
        baritone_build("step", ["~-1", "~-1", "-1"])
        starting_block = offset_block(starting_block, -1, 0, 0)
    goto(starting_block)


def auto_highway() -> None:
    reset_settings()
    x, y, z = get_player_position()
    goto([x, y, 0])
    while not const.FULL_STOP:
        standing_block = get_standing_block()
        step_up_height, contains_snow = get_step_up_height(standing_block)
        if step_up_height >= STEP_HEIGHT_MIN:
            future_step_down_length = get_future_step_down_length(standing_block, step_up_height)
            if future_step_down_length:
                step(standing_block, future_step_down_length)
                continue
            upward_scaffold(step_up_height, contains_snow)
            goto(offset_block(standing_block, 0, 1, 0))
            step_up(step_up_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_up_height, step_up_height + 1, 0))
            continue
        step_down_height, contains_snow = get_step_down_height(standing_block)
        if step_down_height >= STEP_HEIGHT_MIN:
            future_step_up_length = get_future_step_up_length(standing_block, step_down_height)
            if future_step_up_length:
                step(standing_block, future_step_up_length)
                continue
            downward_scaffold(step_down_height, contains_snow)
            goto(offset_block(standing_block, 0, 1, 0))
            step_down(step_down_height, copy.copy(standing_block))
            goto(offset_block(standing_block, -2 * step_down_height, -step_down_height + 1, 0))
            continue
        step(copy.copy(standing_block))


if __name__ == "__main__":
    auto_highway()
    print("Done")
