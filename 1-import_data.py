import pandas as pd

# Importando dados
data = pd.read_excel("Data/VendaCarros.xlsx")
print(data)

# Lista os primeiros registros
# print(data.head())

# Lista os últimos registros
# print(data.tail())

# Contagem de valores por fabricantes
print(data["Fabricante"].value_counts())