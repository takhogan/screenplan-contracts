# ScreenPlan event (grammar 2)
def cleanup():
    Default.Close(query=query, region=region, days=days)

query = parameter('input', default='cats')
region = parameter('select', options=['eu', 'us'])
days = parameter('multiple_select', options=['mon', 'tue'])
with target_host('DESKTOP-01'):
    Default.Search(query=query, region=region, days=days)
    cleanup()
