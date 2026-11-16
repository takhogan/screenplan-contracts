# ScreenPlan event (grammar 2)
count = 3
with target_host('DESKTOP-01'):
    for i in range(count):
        Default.A()
    for j in range(51):
        Default.B()
    for k in range(1, 10, 0):
        Default.C()
    for m in [1, 2]:
        Default.D()
    else:
        Default.E()
    for p, q in [(1, 2)]:
        Default.F()
    for r in 'abc':
        Default.G()
