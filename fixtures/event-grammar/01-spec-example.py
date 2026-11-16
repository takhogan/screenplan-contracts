# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'), target_device('phone0', 'emulator-5554'):
    delay_start(0, 240)
    start_device('phone0')
    try:
        Default.ExampleGame_ToLoadingScreen()
        Default.ExampleGame_DoHourlyTasks()
    finally:
        Default.ExampleGame_Close()
        stop_device('phone0')
