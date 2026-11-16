# ScreenPlan event (grammar 2)
def a():
    b()

def b():
    a()

def c():
    c()

def d():
    a()

with target_host('DESKTOP-01'):
    d()
