import yaml


my_dict = {
    '1$': ['hello', 'world', '!'],
    '2€': 80,
    '3₴': {'hello': 'world', 'goodbye': 'mind'},
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(my_dict, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    f_n_content = yaml.load(f_n)

# должен вывести True
print(f_n_content == my_dict)
