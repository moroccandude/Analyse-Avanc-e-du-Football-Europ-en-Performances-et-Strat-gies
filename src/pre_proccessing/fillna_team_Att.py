import numpy as np
def fillna(X_team):
   little = X_team[X_team['buildUpPlayDribblingClass'] == 'Little']
   x_little = np.random.uniform(24.0, 33.0, little.shape[0])
   X_team.loc[little.index, 'buildUpPlayDribbling'] = x_little

# For 'Normal' class: generate random values between 34 and 66
   normale = X_team[X_team['buildUpPlayDribblingClass'] == 'Normal']
   x_normal = np.random.uniform(34.0, 66.0, normale.shape[0])
   X_team.loc[normale.index, 'buildUpPlayDribbling'] = x_normal

# For 'Lots' class: generate random values between 67 and 77
   lots = X_team[X_team['buildUpPlayDribblingClass'] == 'Lots']
   x_lots = np.random.uniform(67.0, 77.0, lots.shape[0])
   X_team.loc[lots.index, 'buildUpPlayDribbling'] = x_lots
