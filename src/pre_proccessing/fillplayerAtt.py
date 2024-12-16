def filln_player_attribute(df_player_attribute):
    columns_to_fill = [
    'overall_rating', 'potential', 'preferred_foot', 'crossing', 'finishing', 'heading_accuracy',
    'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
    'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
    'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
    'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
    'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
    'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
    'gk_reflexes',
          ]
    for col in columns_to_fill:
      if df_player_attribute[col].dtype == 'object':  # Categorical column
        mode_value = df_player_attribute[col].mode()[0]  # Get the mode (most frequent value)
        df_player_attribute[col].fillna(mode_value, inplace=True)  # Fill NaNs with the mode
      else:  # Numerical column
        mean_value = df_player_attribute[col].mean()  # Calculate the mean
        df_player_attribute[col].fillna(mean_value, inplace=True)  # Fill NaNs with the mean

# Optionally, print the columns to confirm the NaN values have been filled
    print(df_player_attribute[columns_to_fill].isna().sum())
