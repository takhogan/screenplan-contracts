# ScreenPlan event (grammar 2)
Default = 1
len = 3
default.Run()
Default.match()
Default._hidden()
Default.Run(1, query='x')
A.B.C()
make()()
Ops.Report()

def start_device(level=1):
    pass

def seq(level=1):
    pass

def seq(level=2):
    pass

def needs(a, b=1):
    pass

def star(*rest):
    pass

seq(1)
seq(depth=2)
y = missing + 1
z = os.getcwd()
w = Default.Run()
v = seq()
u = open('f')
with target_host('DESKTOP-01'):
    def inner():
        pass
