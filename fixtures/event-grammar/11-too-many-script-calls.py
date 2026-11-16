# ScreenPlan event (grammar 2)
def three():
    Default.A()
    Default.B()
    Default.C()

with target_host('DESKTOP-01'):
    for i in range(50):
        for j in range(3):
            three()
    for k in range(50):
        Default.D()
    Default.E()
