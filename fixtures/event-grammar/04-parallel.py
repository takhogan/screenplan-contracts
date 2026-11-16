# ScreenPlan event (grammar 2)
def helper():
    pass

with target_host('DESKTOP-01'):
    with parallel():
        start_device('phone0', 'emulator-5554')
        query = 'cats'
        Default.Search(query=query)
        extend_end(60, 120)
        if query == 'cats':
            Default.Cats()
        for i in range(2):
            Default.Tick()
        delay_start(0, 10)
        helper()
        with timeout(minutes=5):
            Default.Slow()
        try:
            Default.Guarded()
        finally:
            stop_device('phone0')
