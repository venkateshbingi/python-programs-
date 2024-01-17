# Print a dictionary in table format using loops
input_dict = {1: ["Sam", 21], 2: ["Bob", 25], 3: ["Cara", 30]}
print("ID Name Age")
for key, value in input_dict.items():
    print(f"{key} {value[0]} {value[1]}")
