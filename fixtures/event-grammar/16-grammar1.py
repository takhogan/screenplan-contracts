targetHost('DESKTOP-01')
setWorkspace('Default')
delayStart(0,240)
startDevice('auto')
Windows_DoHourlyTasksShuffle
onDestroy:
    stopDevice('auto')
