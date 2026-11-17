# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    delay_start(30, 90)
    extend_end(900, 900)
    dropout_chance(0.2)
    wait_until(hours=1, minutes=15)
    start_device('phone0')
    start_device('phone0', 'avd:Pixel_7')
    start_device('desktop0', 'DESKTOP-01<>pikvm:office')
    start_device('phone1', 'adb:emulator-5556')
    stop_device('phone1')
    # TODO(grammar 1): targetDevice(emu) -- `emu` isn't set in this event.
    with target_device('DESKTOP-01<>emulator'):
        stop_device('phone0')
        run_event('Daily/Morning run')
