def is_non_full_block(block: str) -> bool:
    return any([
        "snow" in block and "block" not in block,
        "short_grass" in block
    ])
