import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fightLengthInput = input("Enter the fight duration in minutes or seconds (e.g., 5m or 300s): ")

# Parse the fight length input to extract the numeric value and units
fightLengthValue = int(fightLengthInput[:-1])  # Extract numeric part
fightLengthUnit = fightLengthInput[-1]  # Extract unit part

# Convert the fight length to seconds if it's in minutes
if fightLengthUnit == 'm':
    fightLengthValue *= 60  # Convert minutes to seconds

player_times = []
loop_control = int(input("How many players are there?"))
counter = 0

while counter < loop_control:
    userInput = input("Enter the players' time spent alive in seconds or minutes (e.g., 5m or 300s)\n").lower()

    
    playerTimeValue = int(userInput[:-1])  
    playerTimeUnit = userInput[-1]  

    
    if playerTimeUnit == 'm':
        playerTimeValue *= 60  # Convert minutes to seconds

    player_times.append(playerTimeValue)
    counter += 1

life_bias = []

for playerTime in player_times:
    lifeBias = playerTime / fightLengthValue
    life_bias.append(lifeBias)


true_dtps = {}
index = 0
raw_dtps = []
adjusted_dtps = []
counter = 0
while counter < loop_control:
    
    userName = input("Enter the player's name or type 'done' to exit: ").lower()
    if userName == "done":
        break

    player_dtps = float(input("Enter the player's DTPS: "))
    
    raw_dtps.append(player_dtps)
    player_true_dtps = player_dtps / life_bias[index]
    adjusted_dtps.append(player_true_dtps)
    true_dtps[userName] = player_true_dtps
    index += 1
    counter += 1
    
print(true_dtps)
print(raw_dtps)

import numpy as np
import matplotlib.pyplot as plt




players = np.arange(len(raw_dtps))

bar_width = 0.35

# Create a figure and axis for the bar plot
fig, ax = plt.subplots()


raw_bars = ax.bar(players - bar_width / 2, raw_dtps, bar_width, label='Raw DTPS', align='center')
true_bars = ax.bar(players + bar_width / 2, adjusted_dtps, bar_width, label='True DTPS', align='center')


ax.set_xlabel('Player Index')
ax.set_ylabel('DTPS')
ax.set_title('Raw DTPS vs. True DTPS')

# Set x-axis ticks and labels
ax.set_xticks(players)
ax.set_xticklabels(true_dtps.keys())


ax.legend()
num_frames = 100

# Animation function to update the true DTPS bars with interpolation
def animate(i):
    for j, bar in enumerate(true_bars):
        # Use interpolation to smooth the animation
        true_value = adjusted_dtps[j] * (i + 1) / num_frames
        true_bars[j].set_height(true_value)


ani = FuncAnimation(fig, animate, frames=num_frames, interval=20, repeat=False)  # Smaller interval, more frames


plt.tight_layout()
plt.show()
