#Прикрутить  функции к батарейке
import random
class televisor():
    def __init__(self, channel = 0, volume = 0, batareika = random.randint(3, 10)):
        self.channel = channel
        self.volume = volume
        self.batareika = batareika

    def batareika_razradeika(self):
        self.batareika -= 1
    def zaradeika_batareika(self):
        self.batareika = 10

    def switch_volume(self, volume):
        if self.batareika != 0:
            if self.volume != volume:
                self.volume = volume
                self.batareika_razradeika()
            else:
                print('Громкость не может быть такой же')
        else:
            print('Батарейка разрядилась. Поменяй!')

    def switch_channel(self, channel):
        if self.batareika != 0:
            if self.channel != channel:
                self.channel = channel
                self.batareika_razradeika()
            else:
                print('Канал не может быть такой же')
        else:
            print('Батарейка разрядилась. Поменяй!')
    
    def watch(self):
        print('Привки. Я твой верный слуга. Сейчас я нахожусь на канале', self.channel,'.Ты поставил мою громкостьб на', self.volume, '. Заряд батарейки моего пульта -', self.batareika)

def main():
    telik = televisor(int(input('каналь ')), (int(input('громкостьb '))))
    choice = None  
    while choice != "0":
        print \
        ("""
        Мой телевизор
    
        0 - Выйти
        1 - Поменять канал
        2 - Изменить громкось
        3 - Посмотреть на телевизор
        4 - Поменять батарейку
        """)

        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            channell = int(input('введите номер канала(от 1 до 60(включая 60)) '))
            if (channell >= 1) and (channell <= 60):
                telik.switch_channel(channell)
            else:
                print('ты чо слишком умный?')

        # кормление зверюшки
        elif choice == "2":
            volume = int(input('Введите громкость(от 0 до 100) '))
            if (volume >= 0) and (volume <= 100):
                telik.switch_volume(volume)
            else:
                print('ты чо слишком умный?')
        # игра со зверюшкой
        elif choice == "3":
            telik.watch()

        elif choice == "4":
            print('Батарейка поменяна')
            telik.zaradeika_batareika()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice) 
main()