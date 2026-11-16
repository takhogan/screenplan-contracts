# ScreenPlan event (grammar 2)
path = 'Folder/Title'
with target_host('DESKTOP-01'):
    delay_start(1, 2, 3)
    delay_start(1)
    delay_start(1, 2, seconds=3)
    delay_start(1, min_seconds=2)
    delay_start('soon', 10)
    run_event(path)
    stop_device('auto')
    start_device(3)
    dropout_chance(p=[1])
    wait_until()
    wait_until('1h30m')
    with timeout('0h45m'):
        Default.Slow()
    with target_host(5):
        Default.Fast()
    with target_host(['DESKTOP-02', 7]):
        Default.Fast()
kind = parameter('multipleSelect', options=['a'])
pick = parameter('select')
size = parameter('input', 'big')
