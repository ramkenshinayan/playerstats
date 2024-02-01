#import statistical libraries
import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
data = pd.read_csv('players_stats.csv')

# barh(5players x dmg)
plt.figure(1)
plt.barh(data['player'], data['damage'])
plt.title("Total Damage Dealt")
plt.xlabel("Damage")
plt.ylabel("Player")

# pie(5players x gold)

# group bar(5 kda x kda ratio)

# table - mean median mode(games played) 1 team

plt.show()