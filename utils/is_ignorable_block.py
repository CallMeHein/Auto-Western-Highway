__partial_block_names = [
    "air",
    "vine",
    "obsidian",
    "nether",
    "portal",
    "_grass",
    "fern",
    "leaves",
    "_log"
]


def __check_more_specific_conditions(name: str) -> object:
    return any([
        (name.startswith("snow") and "block" not in name),
    ])


def is_ignorable_block(block: str) -> bool:
    """
    :param block: name of the block to be checked
    :return: whether the block should be ignored during ray-casting
    """
    name = block[10:]  # remove the "minecraft:" in front of the block's name
    if any([
        name in ["lily_pad", "dead_bush"],
        any([partialBlockName in name for partialBlockName in __partial_block_names]),
        __check_more_specific_conditions(name)
    ]):
        return True
    return False
