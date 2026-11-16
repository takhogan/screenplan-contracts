# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    if True:
        try:
            Default.D()
        finally:
            Default.E()
    try:
        Default.A()
    except Exception:
        Default.B()
    else:
        Default.C()
try:
    Default.F()
finally:
    Default.G()
