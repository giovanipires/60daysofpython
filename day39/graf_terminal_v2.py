#pip install seaborn
#sudo apt install python3-seaborn
import seaborn as sns
import matplotlib.pyplot as plt

power_levels = {
    "HD FXTSDi": 1450,
    "HD FortyEight": 1200,
    "HD Sportster": 883,
    "HD FatBob": 1600,
    "HD RoadKing": 1800
}

motocicletas = list(power_levels.keys())
cilindradas = list(power_levels.values())

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(x=motocicletas, y=cilindradas, palette="Blues_d")
plt.title("Cilindradas Harley Davidson")
plt.xlabel("Motocicletas")
plt.ylabel("Cilindradas (cc)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()