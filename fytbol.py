class fytbolist:
    total_count = 0
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        fytbolist.total_count += 1
    def predstavlenie(self):
        print('Привет. Меня зовут', self.name, self.surname, '. Моя позиция -', self.position)
    
fytbolist_1 = fytbolist('Лионель', 'Месси', 'нападающий')
fytbolist_2 = fytbolist('Луис', 'Суарес', 'нападающий')
fytbolist_3 = fytbolist('Антуанн', 'Гризманн', 'нападающий')
fytbolist_4 = fytbolist('Серхио ', 'Бускетс', 'полузащитник')
fytbolist_5 = fytbolist('Артур', 'Видаль', 'полузащитник')
fytbolist_6 = fytbolist('Френки де', 'Йонг', 'полузащитник')
fytbolist_7 = fytbolist('Марк-Андре', 'тер Стеген', 'Вратарь')
fytbolist_8 = fytbolist('Жерар', 'Пике', 'защитник')
fytbolist_9 = fytbolist('Клеман', 'Лангле', 'защитник')
fytbolist_10 = fytbolist('Жорди', 'Альба', 'защитник')
fytbolist_11 = fytbolist('Нелсон', 'Семеду', 'защитник')
print(fytbolist.total_count)
print(fytbolist_2.predstavlenie())