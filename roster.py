# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ['Claude', 'Brown', 'Davis'],
          "First Name": ['Ty', 'James', 'RJ'],
          "height": [79, 82, 72],
          "weight": [230,215,180]
          }
data = pd.DataFrame(player)
print(data)
