from package.people import *
from package.salary import *
from datetime import datetime

if __name__ == '__main__':
    class Accountant:
        def __init__(self, name, password):
            self.name = name
            self.password = password

    def Hello():
        print('С возвращением', accountant.name, '!')

    def cheq():
        print(f'Ваша заработная плата на этот месяц составляет {cheque[name]} рублей.')


    accountant = Accountant(name, password)
    print(datetime.today())

    Hello()
    cheq()