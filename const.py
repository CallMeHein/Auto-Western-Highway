STOP_OTHER_THREADS = False
MAX_RAY_STEPS = 20
STEP_HEIGHT_MIN = 1


def isIgnorableBlock(block):
    name = block[10:]
    if any([
        name == "air",
        name.startswith("snow"),
        "obsidian" in name,
        "nether" in name,
        "portal" in name,
        "_grass" in name,
        "fern" in name,
        "leaves" in name,
        "_log" in name
    ]):
        return True
    return False
