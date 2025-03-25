#pip install matplotlib seaborn
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

plt.figure(figsize=(10, 5))
plt.title("Cilindradas Harley Davidson")
plt.xlabel("Motocicletas")
plt.ylabel("Cilindradas (cc)")
plt.bar(motocicletas, cilindradas, color='skyblue')
plt.xticks(rotation=45)  # Rotaciona os nomes para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar cortes
plt.show()