import system.lib.minescript as ms


def reset_settings() -> None:
    ms.chat("#buildRepeat 0,0,0")
    ms.chat("#buildRepeatCount 0")
    ms.chat("#buildInLayers true")
    ms.chat("#layerOrder true")
