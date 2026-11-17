# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    query = 'cats'
    count = 3
    Default.Search(query=query, count=count)
    ACG.Report(query=query, count=count)
    region = 'eu' if count > 2 else 'us'
    Default.DailyReport(query=query, count=count, region=region)
    Default.Search(query=query, count=count, region=region)
