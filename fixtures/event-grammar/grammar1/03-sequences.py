# ScreenPlan event (grammar 2)
def morning():
    note = 'm'
    ACG.Report(name=name, note=note)
    tail(note=note)

def tail(note=None):
    ACG.Close(name=name, note=note)

def evening():
    Default.Close(name=name)

def unused_sequence():
    Default.Close()

with target_host('DESKTOP-01'):
    name = 'first'
    morning()
    evening()
