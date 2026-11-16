# ScreenPlan event (grammar 2)
hour = datetime.datetime.now().hour
with target_host('DESKTOP-01'):
    if hour < 12:
        Default.Morning()
    elif 12 <= hour < 18:
        Default.Afternoon()
    elif hour == 18 or hour == 19:
        pass
    else:
        if random.random() < 0.5:
            Default.Evening()
