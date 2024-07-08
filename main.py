class House:
    def __init__(self, name, number_of_floors): # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor): # Проверка на допустимость этажа
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        for i in range(new_floor):
            j = i + 1
            if new_floor < self.number_of_floors:
                print(j)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)



