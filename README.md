# Auto Western Highway

A script to automatically expand the western overworld highway (-X) on 2b2t

## Prerequisites
- [Baritone](https://github.com/cabaletta/baritone)
- [Minescript](https://github.com/maxuser0/minescript)

## Usage

### Before you launch Minecraft

- move this `auto_highway` folder to your `minescript` folder (default: `.minecraft/minescript`)
- move the schematics to your `schematics` folder (default: `.minecraft/schematics`)
- copy the line(s) from `settings_override.txt` and replace or add them in your baritone settings file (default: `.minecraft/baritone/settings.txt`)

### In-Game

- stand at the end of the highway
- have the following items in your hotbar:
  - Stone Bricks
  - Stone Brick Slabs
  - Smooth Stone
  - Smooth Stone Slabs
  - Dirt
- use `\auto_highway\main`

## Debugging

### PyCharm

- Run > Edit Configurations...
- \+ (Add New Configuration) > Python Debug Server
  - IDE host name: `localhost`
  - Port: `5678`
- Uncomment the `pydevd_pycharm.settrace` and corresponding import in `main.py`
- Run the debugger (Run > Debug)
- Run the script in-game
- It will now break on any set breakpoints