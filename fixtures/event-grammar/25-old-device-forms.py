# ScreenPlan event (grammar 2)
# The one-argument device forms no longer run: a device command names its slot.
with target_host('DESKTOP-01'):
    start_device('avd:Pixel_7')
    with target_device('emulator-5554'):
        Default.CollectRewards()
    with target_device('phone0'):
        Default.CollectRewards()
    stop_device('phone0')
