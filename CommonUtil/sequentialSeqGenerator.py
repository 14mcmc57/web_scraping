# Python doesn't have any mechanism that effectively restricts access to any instance variable or method.
# Python prescribes a convention of prefixing the name of the variable/method with a single or double
# underscore to emulate the behavior of protected and private access specifiers.
# It can still be accessed from outside the class, but the practice should be refrained.

from datetime import date


class Sequencer:
    __letter = 'A'  # 65=A
    __number = 1
    __today = date.today()

    def __init__(self, sim=0):
        if sim > 0:
            self.__number = sim

    def id(self):
        num = self.__number
        self.__number -= -1
        #return "SMT" + self.__today.strftime("%d%m%Y") + chr(self.__letter + 64) + f'{num}'
        return "SMT" + self.__today.strftime("%d%m%Y") + self.__letter  + f'{num}'


obj = Sequencer()


#print(obj.id())
#print(obj.id())
#print(obj.id())
#print(obj.id())
'''
SMT02062021A1
SMT02062021A2
SMT02062021A3
SMT02062021A4

'''