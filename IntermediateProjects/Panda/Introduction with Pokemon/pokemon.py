from numpy import mean
import pandas

data = pandas.read_csv("pokemon.csv")


attack_list = data["Attack"].tolist()
print(mean(attack_list))
print(data["Attack"].mean())
print(data["Attack"].max())
print(data["Attack"].min())

# Get data in columns
names = data.Name
HPs = data.HP
attacks = data.Attack

# Get data in row
print(data.Name[data.Speed == data.Speed.max()])

type_list = data["Type 1"].drop_duplicates().tolist()
print(type_list)
type_list_count = []

for pokemon_type in type_list:
    type_list_count.append(len(data[data["Type 1"] == pokemon_type]))

data_dict = {
    "Type 1": type_list,
    "Count": type_list_count
}

df = pandas.DataFrame(data_dict)
df.to_csv("pokemon_main_types.csv")