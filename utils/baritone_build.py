from types import RelativeXYZ
from utils.async_baritone_command import async_baritone_command
from utils.wait_for_chat import wait_for_chat


def baritone_build(schematic: str, offsets: RelativeXYZ) -> None:
    async_baritone_command(f"#build {schematic}.litematic {offsets[0]} {offsets[1]} {offsets[2]}")
    wait_for_chat("Done building")
