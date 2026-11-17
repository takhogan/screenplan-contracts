# ScreenPlan event (grammar 2)
MODE = parameter('multiple_select', options=['skipTraining','skipTasks'])
LIMIT = parameter('input', default='5')

def runFirst():
    start_device('phone0', 'DESKTOP-01<>bluestacks:One')
    ACCOUNT = 'first'
    Default.Prepare(ACCOUNT=ACCOUNT)
    Default.DoDailyTasks(ACCOUNT=ACCOUNT, MODE=MODE)
    stop_device('phone0', 'DESKTOP-01<>bluestacks:One')

def runSecond():
    Default.DoDailyTasks(MODE=MODE, LIMIT=LIMIT)

with target_host('DESKTOP-01'):
    runFirst()
    runSecond()
