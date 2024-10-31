STOP_OTHER_THREADS = False
FULL_STOP = False
MAX_RAY_STEPS = 20
STEP_HEIGHT_MIN = 1

__partialBlockNames = [
    "vine",
    "obsidian",
    "nether",
    "portal",
    "_grass",
    "fern",
    "leaves",
    "_log"
]


def __checkMoreSpecificConditions(name):
    return any([
        (name.startswith("snow") and "block" not in name),
    ])


def isIgnorableBlock(block):
    """
    :param block: name of the block to be checked
    :return: whether the block should be ignored during ray-casting
    """
    name = block[10:]  # remove the "minecraft:" in front of the block's name
    if any([
        name in ["air", "lily_pad"],
        any([partialBlockName in name for partialBlockName in __partialBlockNames]),
        __checkMoreSpecificConditions(name)
    ]):
        return True
    return False
