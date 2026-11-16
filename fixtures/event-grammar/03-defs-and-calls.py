# ScreenPlan event (grammar 2)
def session(rounds=1, label='main'):
    start_device('phone0')
    Default.Play(rounds=rounds, label=label)
    stop_device('phone0')

def twice():
    session(rounds=2)
    session(label='second')

with target_host(['DESKTOP-01', 'DESKTOP-02']):
    twice()
    with timeout(minutes=30), restart_device_on_crash():
        session()
