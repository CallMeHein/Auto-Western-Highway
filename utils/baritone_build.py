from type_annotations import XYZ
from utils.async_baritone_command import async_baritone_command
from utils.wait_for_chat import wait_for_chat


def baritone_build(schematic: str, coordinates: XYZ) -> None:
    async_baritone_command(f"#build {schematic}.litematic {coordinates[0]} {coordinates[1]} {coordinates[2]}")
    wait_for_chat("Done building")
