# ScreenPlan event (grammar 2)
ops = 1
unused = 'x'
with target_host('DESKTOP-01'), target_device('phone0', 'emulator-9999'):
    Default.Search(query='cats', extra=1)
    Default.Search()
    Default.Missing()
    Nope.Run()
    Default.NotHere()
    run_event('Folder/Title', region='eu', size=2)
    run_event('Folder/Missing')
with target_host('UNKNOWN-HOST'):
    Default.Search(query='dogs')
with target_host('office'):
    Default.Search(query='birds')
start_device('phone1', 'emulator-0000')
Default.Search(query=ops)
