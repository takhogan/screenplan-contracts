# ScreenPlan event (grammar 2)
def parked():
    Default.Close()

# morning run
with target_host('DESKTOP-01'):
    # grammar 1 ignored this line: endExtension(900,900)
    # grammar 1 ignored this line (it names no device): targetDevice('phone0')
    Default.Play()
