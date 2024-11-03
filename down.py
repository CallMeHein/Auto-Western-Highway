import copy
from typing import List

import system.lib.minescript as ms
from const import MAX_RAY_STEPS, FUTURE_STEPS
from logger import logger
from utils.is_non_full_block import is_non_full_block
from utils.reset_settings import reset_settings
from type_annotations import XYZ
from utils.baritone_build import baritone_build
from utils.is_ignorable_block import is_ignorable_block
from utils.offset_block import offset_block


def step_down(count: int, build_origin: XYZ) -> XYZ:
    logger.write_log(f"step_down: {count}")
    build_origin = offset_block(build_origin, 0, 1, 0)
    for _ in range(count):
        baritone_build("step_down", offset_block(build_origin, -1, -1, -1))
        baritone_build("step", offset_block(build_origin, -2, -2, -1))
        build_origin = offset_block(build_origin, -2, -1, 0)
    return offset_block(build_origin, 0, -1, 0)


def downward_scaffold(count: int, contains_non_full_block: bool, build_origin: XYZ) -> None:
    logger.write_log(f"scaffold_down: {count}")
    ms.chat(f"#buildIgnoreExisting {str(not contains_non_full_block).lower()}")
    ms.chat("#buildRepeat 2,1,0")
    ms.chat(f"#buildRepeatCount {count}")
    baritone_build("step_scaffold", offset_block(build_origin, -2 * count, -count, 0))
    reset_settings()


def get_step_down_height(standing_block: XYZ) -> tuple[int, bool]:
    ray_up_blocks = ms.getblocklist(get_down_ray_blocks(standing_block))
    contains_non_full_block = any([is_non_full_block(block) for block in ray_up_blocks])
    step_down_height = 0
    for step_count in range(MAX_RAY_STEPS):
        blocks = [
            ray_up_blocks[step_count * 3 + 0],
            ray_up_blocks[step_count * 3 + 1],
            ray_up_blocks[step_count * 3 + 2],
        ]
        if step_count == 0 and is_ignorable_block(blocks[1]) and is_ignorable_block(blocks[2]):
            step_down_height += 1
        elif all([is_ignorable_block(block) for block in blocks]):
            step_down_height += 1
        else:
            break
    return step_down_height, contains_non_full_block


def get_future_step_down_length(standing_block: XYZ, step_up_height: int) -> int:
    step_up_block = offset_block(copy.copy(standing_block), -2 * step_up_height, step_up_height, 0)
    for future_step in range(FUTURE_STEPS):
        future_block = offset_block(step_up_block, -future_step, 0, 0)
        future_step_down_height, _ = get_step_down_height(future_block)
        if future_step_down_height >= step_up_height:
            return 4 * step_up_height + future_step
    return 0


def get_down_ray_blocks(standing_block: XYZ) -> List[XYZ]:
    blocks = [offset_block(standing_block, 0, 1, 0)]
    for _ in range(MAX_RAY_STEPS):
        step_start_pos = copy.copy(blocks[-1])
        step_start_pos[1] -= 1
        for block in range(3):
            block_pos = copy.copy(step_start_pos)
            block_pos[0] -= block
            blocks.append(block_pos)
    return blocks[1:]
