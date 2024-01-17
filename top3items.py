input_dict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
top_items = sorted(input_dict, key=input_dict.get, reverse=True)[:3]
print(top_items)