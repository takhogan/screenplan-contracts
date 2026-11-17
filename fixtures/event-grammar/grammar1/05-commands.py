# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    delay_start(30, 90)
    extend_end(900, 900)
    dropout_chance(0.2)
    wait_until(hours=1, minutes=15)
    # TODO(grammar 1): startDevice('auto') -- the one-argument form no longer runs, nor does this event today: write start_device('phone0'), checking the slot
    # TODO(grammar 1): startDevice('avd:Pixel_7') -- the one-argument form no longer runs, nor does this event today: write start_device('phone0', 'avd:Pixel_7'), checking the slot
    # TODO(grammar 1): startDevice('DESKTOP-01<>pikvm:office') -- the one-argument form no longer runs, nor does this event today: write start_device('desktop0', 'DESKTOP-01<>pikvm:office'), checking the slot
    start_device('phone1', 'adb:emulator-5556')
    stop_device('phone1')
    # TODO(grammar 1): targetDevice(emu) -- the one-argument form no longer runs, nor does this event today: write with target_device('phone0', emu):, checking the slot
    # TODO(grammar 1): targetDevice('DESKTOP-01<>emulator') -- the one-argument form no longer runs, nor does this event today: write with target_device('phone0', 'DESKTOP-01<>emulator'):, checking the slot
    # TODO(grammar 1): stopDevice(auto) -- the one-argument form no longer runs, nor does this event today: write stop_device('phone0'), checking the slot
    run_event('Daily/Morning run')
