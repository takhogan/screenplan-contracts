# ScreenPlan event (grammar 2)
items = ['a', 'b', 'c']
settings = {'speed': 2, 'mode': 'fast'}
pause = random.randint(10, 20) * 2 + math.floor(math.pi)
first = items[0] if len(items) > 0 else None
part = items[1:]
later = datetime.datetime.now() + datetime.timedelta(minutes=5)
label = str(round(max(1.5, min(3, 2)), 1)) + '-' + random.choice(items)
weekday = datetime.datetime.now().weekday()
ok = not (pause > 100) and 'a' in items
with target_host('DESKTOP-01'), timeout(hours=1, minutes=30):
    with target_device('phone0', 'emulator-5554'), restart_device_on_crash('emulator-5554'):
        Default.Run(pause=pause, first=first, part=part, later=later, label=label, weekday=weekday, ok=ok, speed=settings['speed'])
    dropout_chance(0.2)
    wait_until(minutes=45)
    run_event('Daily/Reports', region='eu')
    pass
