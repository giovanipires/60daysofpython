#pip install plotext
#python3 -m pip install plotext --break-system-packges
#sudo apt install python3-plotext

import plotext as plt

power_levels = {
    "HD FXTSDi": 1450,
    "HD FortyEight": 1200,
    "HD Sportster": 883,
    "HD FatBob": 1600,
    "HD RoadKing": 1800
}

motocicletas = list(power_levels.keys())
cilindradas = list(power_levels.values())

plt.title("Cilindradas Harley Davidson")

plt.xlabel("Motocicletas")
plt.ylabel("Cilindradas")

plt.bar(motocicletas, cilindradas, label="Cilindradas")

plt.show()