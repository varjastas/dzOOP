import random
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

crit_sp = []
def main():
    for i in range(0, int(input('Сколько зверушек создатб?'))):
        crit_name = input("Как вы назовете свою зверюшку?: ")
        crit = Critter(crit_name)
        crit_sp.append(crit)
    print(crit_sp)
    choice = None  
    while choice != "0":
        print \
        ("""
        Моя ферма
    
        0 - Выйти
        1 - Узнать о самочувствии фермы
        2 - Покормить ферму
        3 - Поиграть с фермой
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            for i in range(0, len(crit_sp)):
                crit_sp[i].talk()

        # кормление зверюшки
        elif choice == "2":
            eat = int(input('Сколько дать еды(1 = 100 г)' ))
            print("Мррр...  Спасибо!")
            for i in crit_sp:
                
                i.eat(eat)
         
        # игра со зверюшкой
        elif choice == "3":
            play = int(input('Сколько играться(1 = 10 мин)' ))
            print('Уииии!')
            for i in crit_sp:
                
                i.play(play)

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
