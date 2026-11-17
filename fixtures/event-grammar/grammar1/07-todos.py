# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    # TODO(grammar 1): files=os.listdir('.') -- `os.listdir()` can't be called in an expression: the functions are len, str, int, float, min, max, round, random.random, random.randint, random.choice, math.*, datetime.datetime.now and datetime.timedelta.
    t = '0h30m'
    # TODO(grammar 1): timeout(t) -- timeout needs a duration written as '1h30m'
    # TODO(grammar 1): if(len(files) > 2, Report) -- grammar 1 crashed on if(…) when its condition held: write an if block
    # TODO(grammar 1): My-Script -- rename this script to call it from an event
    # TODO(grammar 1): Report -- the workspace `ops` isn't a ScreenPlan name: rename it to call its scripts from an event
    # TODO(grammar 1): Report -- the workspace is set from a value only known when the event runs
    # TODO(grammar 1): startDevice('DESKTOP-01<>emulator') -- the device name has no device-type prefix (a device mapping keyword?): name the slot
