def assign_match_results(x):
    # Default values (None) to columns
    x['won_home_team'] = 'won' if x['home_team_goal'] > x['away_team_goal'] else None
    x['won_away_team'] = 'won' if x['home_team_goal'] < x['away_team_goal'] else None
    x['loss_home_team'] = 'loss' if x['home_team_goal'] < x['away_team_goal'] else None
    x['loss_away_team'] = 'loss' if x['home_team_goal'] > x['away_team_goal'] else None
    x['null'] = 1  
    return x
