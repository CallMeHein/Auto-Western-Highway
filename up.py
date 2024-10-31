import copy
from typing import List

import system.lib.minescript as ms
from annotations import XYZ
from const import MAX_RAY_STEPS
from utils.goto import goto
from utils.is_ignorable_block import is_ignorable_block
from utils.offset_block import offset_block
from utils.wait_for_chat import wait_for_chat


def step_up(count: int, starting_block: XYZ) -> None:
    starting_block = offset_block(starting_block, 0, 1, 0)
    for _ in range(count):
        goto(starting_block)
        ms.chat("#build step_up.litematic ~-2 ~ -1")
        starting_block = offset_block(starting_block, -2, 1, 0)
        wait_for_chat("Done building")


def upward_scaffold(count: int) -> None:
    ms.chat("#buildIgnoreExisting false")
    ms.chat("#buildRepeat -2,1,0")
    ms.chat(f"#buildRepeatCount {count}")
    ms.chat(f"#build step_scaffold.litematic ~-3 ~ 0")
    wait_for_chat("Done building")

    ms.chat("#buildRepeat 0,0,0")
    ms.chat("#buildRepeatCount 0")


def get_step_up_height(standing_block: XYZ) -> int:
    ray_up_blocks = ms.getblocklist(get_up_ray_blocks(standing_block))
    if all([is_ignorable_block(block) for block in ray_up_blocks]):
        return 0
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
    return step_up_height


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
