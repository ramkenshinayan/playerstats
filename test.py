#import statistical libraries
import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
data = pd.read_csv('players_stats.csv')

# barh(1 team x dmg)
figure1_rows = pd.DataFrame(data, columns=['team', 'player', 'damage'])
teamName = 'INTZ'
team = figure1_rows[figure1_rows['team'] == teamName]
players = team['player'].tolist()
damage = team['damage'].tolist()

plt.figure(1)
plt.barh(players, damage)
plt.title("Total Damage Dealt by " + teamName)
plt.xlabel("Damage")
plt.ylabel("Player")

# pie(1 team x gold)
figure2_rows = pd.DataFrame(data, columns=['team', 'player', 'gold'])
teamName = 'INTZ'
team = figure2_rows[figure2_rows['team'] == teamName]

plt.figure(2)
plt.pie(team['gold'], labels=team['player'])
plt.title(teamName + " gold")

# group bar(5 kda x kda ratio)

# table - mean median mode(games played) 1 team

plt.show()