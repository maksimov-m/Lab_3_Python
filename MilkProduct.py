from Product import *

class MilkProduct(Product):
    def __init__(self, name, producer, term, fat):
        super().__init__(name, producer, term)
        self.__fat = fat

    @property
    def fat(self):
        return self.__fat

    def __str__(self):
        return super().__str__() + f"\nFat : {self.fat}"

    def __del__(self):
        super().__del__()

    def add(self):
        if(not self.el_in_mass(self)):
            if Merch.begin == None:
                self.next = Merch.begin

                Merch.begin = self
                Merch.end = self
                Merch.count += 1
            else:
                self.next = Merch.begin

                Merch.begin = self
                Merch.count += 1