#import statistical libraries
import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
data = pd.read_csv('players_stats.csv')

# barh(1 team x dmg)
rows = pd.DataFrame(data, columns=['team', 'player', 'damage'])
teamName = 'INTZ'
team = rows[rows['team'] == teamName]
players = team['player'].tolist()
damage = team['damage'].tolist()

plt.figure(1)
plt.barh(players, damage)
plt.title("Total Damage Dealt by " + teamName)
plt.xlabel("Damage")
plt.ylabel("Player")

# pie(5 players x gold)

# group bar(5 kda x kda ratio)

# table - mean median mode(games played) 1 team

plt.show()