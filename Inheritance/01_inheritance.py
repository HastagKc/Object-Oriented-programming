class Human:
    def eat(self):
        print('I can eat')

    def work(self):
        print('I can work')

class Men(Human):
    pass

man1 = Men()

man1.eat()
man1.work()