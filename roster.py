# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ['Claude', 'Brown', 'Davis']
player = {"Last Name": roster,
          "First Name": ['Ty', 'James', 'RJ'],
          "height": [79, 82, 72],
          "weight": [230,215,180]}
data = pd.DataFrame(player)
print(data)
