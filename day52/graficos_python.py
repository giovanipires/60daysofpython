import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D"]
valores = [1, 10, 100, 1000]
soma_valores = sum(valores)
labels_legenda = []
for i in range(len(categorias)):
    porcentagem = round((valores[i] / soma_valores) *100, 1)
    labels_legenda.append(f"{categorias[i]} - {porcentagem}%")

fig, ax = plt.subplots(figsize=(8,8))

patches, texts = ax.pie(
    valores,
    labels=None,
    startangle=140
)

ax.legend(patches, labels_legenda, title="Categorias", loc="best")

# plt.figure(figsize=(10, 10))
# plt.pie(valores, 
#         labels=None, 
#         autopct='%1.1f%%', 
#         startangle=140, 
#         labeldistance=1.1, 
#         pctdistance=1.25
#         )
plt.title("Gráfico de pizza")
plt.show()
