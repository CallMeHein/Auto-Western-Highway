from type_annotations import XYZ


def offset_block(block: XYZ, x_off: int, y_off: int, z_off: int) -> XYZ:
    """
    :return: [x, y, z] of block, offset by x_off, y_off, z_off
    """
    return [block[0] + x_off, block[1] + y_off, block[2] + z_off]
