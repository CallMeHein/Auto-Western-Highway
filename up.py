import copy
from typing import List

import system.lib.minescript as ms
from const import MAX_RAY_STEPS, FUTURE_STEPS
from logger import logger
from utils.is_snow import is_snow
from utils.reset_settings import reset_settings
from type_annotations import XYZ
from utils.baritone_build import baritone_build
from utils.goto import goto
from utils.is_ignorable_block import is_ignorable_block
from utils.offset_block import offset_block


def step_up(count: int, starting_block: XYZ) -> None:
    logger.write_log(f"step_up: {count}")
    starting_block = offset_block(starting_block, 0, 1, 0)
    for _ in range(count):
        goto(starting_block)
        starting_block = offset_block(starting_block, -2, 1, 0)
        baritone_build("step_up", ["~-2", "~", "-1"])


def upward_scaffold(count: int, contains_snow: bool) -> None:
    logger.write_log(f"scaffold_up: {count}")
    ms.chat(f"#buildIgnoreExisting {str(not contains_snow).lower()}")
    ms.chat("#buildRepeat -2,1,0")
    ms.chat(f"#buildRepeatCount {count}")
    baritone_build("step_scaffold", ["~-3", "~", "0"])
    reset_settings()


def get_step_up_height(standing_block: XYZ) -> tuple[int, bool]:
    ray_up_blocks = ms.getblocklist(get_up_ray_blocks(standing_block))
    contains_snow = any([is_snow(block) for block in ray_up_blocks])
    if all([is_ignorable_block(block) for block in ray_up_blocks]):
        return 0, False
    step_up_height = 1
    for step_count in range(MAX_RAY_STEPS):
        blocks = [
            ray_up_blocks[step_count * 3 + 0],
            ray_up_blocks[step_count * 3 + 1],
            ray_up_blocks[step_count * 3 + 2],
        ]
        if all([is_ignorable_block(block) for block in blocks]):
            step_up_height += 1
        else:
            break
    return step_up_height, contains_snow


def get_future_step_up_length(standing_block: XYZ, step_down_height: int) -> int:
    step_up_block = offset_block(copy.copy(standing_block), -2 * step_down_height, -step_down_height, 0)
    for future_step in range(FUTURE_STEPS):
        future_block = offset_block(step_up_block, -future_step, 0, 0)
        future_step_down_height, _ = get_step_up_height(future_block)
        if future_step_down_height >= step_down_height:
            return 4 * step_down_height + future_step
    return 0


def get_up_ray_blocks(standing_block: XYZ) -> List[XYZ]:
    blocks = [standing_block]
    for _ in range(MAX_RAY_STEPS):
        step_start_pos = copy.copy(blocks[-1])
        step_start_pos[1] += 1
        for block in range(3):
            block_pos = copy.copy(step_start_pos)
            block_pos[0] -= block
            blocks.append(block_pos)
    return blocks[1:]
