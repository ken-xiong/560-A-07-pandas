# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ['Claude', 'Brown', 'Davis', 'Tyson', 'Jackson', 'Holbrook', 'Trimble', 'Cadeau', 'Davis', 'Powell'],
          "First Name": ['Ty', 'James', 'RJ', 'Cade', 'Ian', 'John', 'Seth', 'Elliot', 'Elijah', 'Drake'],
          "height": [79, 82, 72, 79, 76, 80, 75, 73, 75, 78],
          "weight": [230, 215, 180, 200, 190, 230, 195, 180, 215, 195]
}

data = pd.DataFrame(player)

#bmi = weight in kg/ height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")