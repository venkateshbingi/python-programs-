# Create and display all combinations of letters from a dictionary
input_dict = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [x + y for x in input_dict['1'] for y in input_dict['2']]
print(combinations)
