# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    delay_start(0, 240)
    try:
        start_device('phone0')
        Default.Windows_DoHourlyTasksShuffle()
    finally:
        stop_device('phone0')
