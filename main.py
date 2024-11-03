import copy
import const
from const import STEP_HEIGHT_MIN
from down import get_step_down_height, downward_scaffold, step_down, get_future_step_down_length
from logger import logger
from utils.reset_settings import reset_settings
from type_annotations import XYZ
from up import get_step_up_height, upward_scaffold, step_up, get_future_step_up_length
from utils.baritone_build import baritone_build
from utils.get_standing_block import get_standing_block
from utils.offset_block import offset_block

# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True, suspend=False)


def step(build_origin: XYZ, count=1) -> XYZ:
    logger.write_log(f"step: {count}")
    for _ in range(count):
        baritone_build("step", offset_block(build_origin, -1, 0, -1))
        build_origin = offset_block(build_origin, -1, 0, 0)
    return build_origin


def auto_highway() -> None:
    reset_settings()
    standing_block = get_standing_block()
    standing_block[2] = 0
    while not const.FULL_STOP:
        step_up_height, contains_non_full_block = get_step_up_height(standing_block)
        if step_up_height >= STEP_HEIGHT_MIN:
            future_step_down_length = get_future_step_down_length(standing_block, step_up_height)
            if future_step_down_length:
                standing_block = step(standing_block, future_step_down_length)
                continue
            upward_scaffold(step_up_height, contains_non_full_block, copy.copy(standing_block))
            standing_block = step_up(step_up_height, standing_block)
            continue
        step_down_height, contains_non_full_block = get_step_down_height(standing_block)
        if step_down_height >= STEP_HEIGHT_MIN:
            future_step_up_length = get_future_step_up_length(standing_block, step_down_height)
            if future_step_up_length:
                standing_block = step(standing_block, future_step_up_length)
                continue
            downward_scaffold(step_down_height, contains_non_full_block, copy.copy(standing_block))
            standing_block = step_down(step_down_height, standing_block)
            continue
        standing_block = step(standing_block)


if __name__ == "__main__":
    auto_highway()
    print("Done")
