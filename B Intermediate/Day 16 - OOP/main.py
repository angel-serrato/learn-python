import requests
from prettytable import PrettyTable

url = "https://pokeapi.co/api/v2/pokemon/"
num_pokemon = 10
pokemons = []

for i in range(1, num_pokemon + 1):
    response = requests.get(f"{url}{i}")
    data = response.json()
    name = data['name']
    types = [t['type']['name'] for t in data['types']]
    pokemons.append({"ID": i, "Name": name.capitalize(), "Types": ", ".join(types)})

table = PrettyTable()
table.field_names = ["ID", "Name", "Types"]

for pokemon in pokemons:
    table.add_row([pokemon["ID"], pokemon["Name"], pokemon["Types"]])

table.align = "r"
print(table)

# table = PrettyTable()
# table.field_names = ["Uno","Dos","Tres"]
# table.add_row(["Angel", 1987, 500])
# table.add_row(["Didier", 1987, 500])
# table.add_row(["Serrato", 1987, 500])
# table.add_row(["Arias", 1987, 500])
# print(table)