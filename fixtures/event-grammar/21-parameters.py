# ScreenPlan event (grammar 2)
region = parameter('select', options=['eu', 'us'])
rounds = parameter('input', default=3)
tags = parameter('multiple_select', options=['a', 'b'])

def inner():
    level = parameter('input', default=1)
    Default.Use(level=level)

with target_host('DESKTOP-01'):
    Default.Report(region=region, rounds=rounds, tags=tags, title=f'Report {region!r:>4}')
    inner()
