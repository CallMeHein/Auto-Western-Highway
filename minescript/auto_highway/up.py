import copy

import system.lib.minescript as ms
from auto_highway.const import MAX_RAY_STEPS, isIgnorableBlock
from auto_highway.util import wait_for_chat



def step_up(count):
    ms.chat("#buildRepeat -2,1,0")
    ms.chat(f"#buildRepeatCount {count}")
    ms.chat("#build step_up.litematic ~-2 ~ -1")
    wait_for_chat("Done building")

    ms.chat("#buildRepeat 0,0,0")
    ms.chat("#buildRepeatCount 0")


def upward_scaffold(count):
    ms.chat("#buildIgnoreExisting false")
    ms.chat("#buildRepeat -2,1,0")
    ms.chat(f"#buildRepeatCount {count}")
    ms.chat(f"#build step_scaffold.litematic ~-3 ~ 0")
    wait_for_chat("Done building")

    ms.chat("#buildRepeat 0,0,0")
    ms.chat("#buildRepeatCount 0")


def should_step_up(standing_block):
    ray_up_blocks = ms.getblocklist(get_up_ray_blocks(standing_block))
    if all([isIgnorableBlock(block) for block in ray_up_blocks]):
        return 0
    step_up_height = 1
    for step_count in range(MAX_RAY_STEPS):
        blocks = [
            ray_up_blocks[step_count * 3 + 0],
            ray_up_blocks[step_count * 3 + 1],
            ray_up_blocks[step_count * 3 + 2],
        ]
        if all([isIgnorableBlock(block) for block in blocks]):
            step_up_height += 1
        else:
            break
    return step_up_height


def get_up_ray_blocks(standing_block):
    blocks = [standing_block]
    for _ in range(MAX_RAY_STEPS):
        step_start_pos = copy.copy(blocks[-1])
        step_start_pos[1] += 1
        for block in range(3):
            block_pos = copy.copy(step_start_pos)
            block_pos[0] -= block
            blocks.append(block_pos)
    return blocks[1:]
