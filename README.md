# Auto Western Highway

A script to automatically expand the western overworld highway (-X) on 2b2t

# Disclaimer

This is still a WIP and should not be used without supervision. Baritone likes to get stuck and the script does not always make correct decisions yet. Manual interference is sometimes needed.

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

### Troubleshooting
Some baritone settings may affect performance or cause the script to get stuck

#### Gets stuck while placing blocks:
- blockReachDistance may be too low

#### Gets stuck while breaking blocks:
- blockBreakSpeed may be too low

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

## TODOs

- when scaffolding down, build out a support to ensure that the first step does not get stuck (like it currently does on water)
- separate terminal window to log this script's decisions. The in-game chat is currently useless because of the flood of Baritone's logs.
  - allow the user to write commands which will be executed in the in-game chat? Depending on client/active modules, you may not have full control over the in-game chat.