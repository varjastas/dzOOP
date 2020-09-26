#Прикрутить  функции к батарейке
import random
class televisor():
    def __init__(self, channel = 0, volume = 0, batareika = random.randint(3, 10)):
        self.__channel = channel
        self.__volume = volume
        self.__batareika = batareika
    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, newValue):
        if self.__batareika != 0:
            if 0 < newValue < 61:
                self.__channel = newValue 
            else:
                print('Нету такого канала')
        else:
            print('Оуооооуоуу.Селааааа батарейка.')

    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self,newValue):
        if self.__batareika != 0:
            if -1 < newValue < 101:
                self.__volume = newValue 
            else:
                print('Неправильная громкость')
        else:
            print('Оуооооуоуу.Селааааа батарейка.')

    def __batareika_razradeika(self):
        self.__batareika -= 1
    def zaradeika_batareika(self):
        self.__batareika = 10


    def watch(self):
        print('Привки. Я твой верный слуга. Сейчас я нахожусь на канале', self.__channel,'.Ты поставил мою громкостьб на', self.__volume, '. Заряд батарейки моего пульта -', self.__batareika)

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
            telik.channel = channell

        # кормление зверюшки
        elif choice == "2":
            volume = int(input('Введите громкость(от 0 до 100) '))
            telik.volume = volume
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