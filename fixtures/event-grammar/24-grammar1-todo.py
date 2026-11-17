# ScreenPlan event (grammar 2)
with target_host('DESKTOP-01'):
    Default.Search()
    # TODO(grammar 1): if(x > 1, Report) -- grammar 1 crashed on if(…) when its condition held: write an if block
    Default.Report()
