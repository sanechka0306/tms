import json

data = {
    123456: ('Андрей', 18),
    789456: ('Игорь', 19),
    123779: ('Валерия', 20),
    123799: ('Валера', 22),
    123790: ('Валя', 22),
}

with open('data.json', 'w') as f:
    temp = json.dumps(data, sort_keys=True, indent=4)
    f.write(temp)
