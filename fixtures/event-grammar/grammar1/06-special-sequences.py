# ScreenPlan event (grammar 2)
# onError was dropped: grammar 1 never ran it.
#   onError:
#   Recover

# onInit's lines come first. Grammar 1 crashed on every event with an onInit, so this event never ran before: check it.
start_device('phone0', 'adb:emulator-5554')
with target_host('DESKTOP-01'):
    level = 3
    dropout_chance(0.1)
    try:
        Default.Play(level=level)
    finally:
        Default.Close(level=level)
        stop_device('phone0')
