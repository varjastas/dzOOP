import random
'''
В классе криттер происходит инициализация каждого существа и управление каждым отдельно.
В классе зооферма происходит управление всеми сразу и сбор всех криттеров в зооферму
'''
class Zooferma:
    def __init__(self, kol_zver):
        self.crit_sp = []
        for i in range(0, kol_zver):
            name = input('Введите имя зверя')
            self.crit_sp.append(Critter(name))

    def create_new_zver(self):
        name = input('Ввеите имя зверушки')
        if (name != '') and (name != ' '):
            self.crit_sp.append( Critter(name))
        else:
            print('Имя не может быть пустой строкой')
    
    def feed_solo(self):
        number = int(input('Введите номер зверушки(начиная с 0)'))
        eat = int(input('Сколько дать есть. 1 = 100г'))
        self.crit_sp[number].eat(eat)

    def feed_all(self):
        eat = int(input('Сколько дать есть. 1 = 100г'))
        for i in self.crit_sp:
            i.eat(eat)

    def play_solo(self):
        number = int(input('Введите номер зверушки(начиная с 0)'))
        play = int(input('Сколько играть. 1 = 5 мин'))
        self.crit_sp[number].play(play)

    def play_all(self):
        play = int(input('Сколько играть. 1 = 5 мин'))
        for i in self.crit_sp:
            i.play(play)

    def talk_solo(self):
        number = int(input('Введите номер зверушки(начиная с 0)'))
        self.crit_sp[number].talk()
        
    def talk_all(self):

        for i in self.crit_sp:
            i.talk()
class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name):
        self.__name = name
        self.hunger = random.randint(0, 10)
        self.boredom = random.randint(0, 10)
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, 
            ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    choice = None  
    Volk_v_Circe = Zooferma(int(input('Начальное кол-во зверей'))) 
    while choice != "0":
        print \
        ("""
        Моя ферма
    
        0 - Выйти
        1 - Узнать о самочувствии фермы
        2 - Узнать о самочувствии отдельной зверушки
        3 - Покормить ферму
        4 - Покормить отдельную зверушку
        5 - Поиграть с фермой
        6 - Поиграть с отдельной зверушкой
        7 - Создать зверушку
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        #Узнать о самочувствии фермы
        elif choice == "1":
            Volk_v_Circe.talk_all()

        # Узнать о самочувствии отдельной зверушки
        elif choice == "2":
            Volk_v_Circe.talk_solo()

        #Покормить ферму
        elif choice == "3":
            Volk_v_Circe.feed_all()

        #Покормить отдельную зверушку
        elif choice == "4":
            Volk_v_Circe.feed_solo()

        #Поиграть с фермой
        elif choice == "5":
            Volk_v_Circe.play_all()
        
        #Поиграть с отдельной зверушкой
        elif choice == "6":
            Volk_v_Circe.play_solo()

        elif choice == "7":
            Volk_v_Circe.create_new_zver()

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
