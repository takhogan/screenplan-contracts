# ScreenPlan event (grammar 2)
def loop():
    # TODO(grammar 1): loop -- a sequence that calls itself: grammar 1 crashed on it
    pass

def step():
    Default.Run()

with target_host('DESKTOP-01'):
    loop()
    # TODO(grammar 1): step -- this sequence is called from places with different variables or workspaces: pass them by hand
    extra = 'x'
    # TODO(grammar 1): step -- this sequence is called from places with different variables or workspaces: pass them by hand
