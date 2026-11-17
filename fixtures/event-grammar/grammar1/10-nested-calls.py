# ScreenPlan event (grammar 2)
def outer():
    mode = 'fast'
    inner(mode=mode)

def inner(mode=None):
    Default.Run(mode=mode)

with target_host('DESKTOP-01'):
    outer()
