class Student:
    def __init__(self, firstname='Денис', lastname='Рыжий', age=18, group_number=11004218):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.group_number = group_number

    def get_full_name(self):
        return self.firstname, self.lastname

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        print("Данные были изменены!")

    def set_group_number(self, group_number: int):
        self.group_number = group_number
        print("Данные были изменены!")


a = [
    Student('Иван', 'Соколов', 18, 11004318),
    Student('Игорь', 'Воробьев', 11004118),
    Student('Алексей', 'Скворцов', 18, 11004319),
    Student('Валера', 'Ворона', 18)
]

print(*a[3].get_full_name(), '\n' + 'Возраст:', a[3].get_age(), '\n' + 'Группа:', a[3].get_group_number())
