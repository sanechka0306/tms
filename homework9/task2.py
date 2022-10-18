import json

with open("data.json") as f:
    data = json.load(f)


class Data:
    def data(self):
        return f'Пользователь id123456: {self.id123456[0]}, {self.id123456[1]} лет \n' \
               f'Пользователь id123779: {self.id123779[0]}, {self.id123779[1]} лет'


User = type("User_2", (Data,), data)
New_user = User()
print(New_user.data())
