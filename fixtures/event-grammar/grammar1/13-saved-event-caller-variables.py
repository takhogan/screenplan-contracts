# ScreenPlan event (grammar 2)
# Set by the event that runs this one: grammar 1 let a saved event read its variables.
ACCOUNT = parameter('input')

DEVICES = {"first":"DESKTOP-01<>bluestacks:One","second":"DESKTOP-01<>bluestacks:Two"}
targetDevice = DEVICES[ACCOUNT]
with target_device('phone0', targetDevice):
    try:
        start_device('phone0')
        Default.Prepare(ACCOUNT=ACCOUNT, DEVICES=DEVICES, targetDevice=targetDevice)
        Default.Report(ACCOUNT=ACCOUNT, DEVICES=DEVICES, targetDevice=targetDevice)
        stop_device('phone0')
    finally:
        stop_device('phone0')
