# ScreenPlan event (grammar 2)
with target_host(['DESKTOP-01', 'DESKTOP-02']), target_device('phone0', 'bluestacks:Pie64'), restart_device_on_crash():
    Default.OpenGame()
    with timeout(hours=2):
        with parallel():
            Default.CollectRewards()
            Default.CollectMail()
        with timeout(minutes=30), restart_device_on_crash('DESKTOP-01<>bluestacks:Pie64'), target_host('DESKTOP-02'):
            Default.CloseGame()
