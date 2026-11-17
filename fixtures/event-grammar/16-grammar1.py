targetHost('DESKTOP-01')
setWorkspace('Default')
delayStart(0,240)
startDevice('phone0')
Windows_DoHourlyTasksShuffle
onDestroy:
    stopDevice('phone0')
