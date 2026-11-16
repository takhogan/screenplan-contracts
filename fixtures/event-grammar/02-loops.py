# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    for region in ['eu', 'us']:
        Default.DailyReport(region=region)

    for i in range(3):
        Default.CollectRewards()
        delay_start(30, 90)

    for n in range(-2, 4, 3):
        for t in ('a', 'b'):
            Default.Pair(n=n, t=t)
