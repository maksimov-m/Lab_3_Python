from Merch import *

class Product(Merch):
    def __init__(self, name, producer, term):
        super().__init__(name, producer)
        self.__term = term

    @property
    def term(self):
        return self.__term

    def __str__(self):
        return super().__str__() + f"\nTerm : {self.term}"

    def add(self):
        if (not self.el_in_mass(self)):
            if Merch.begin == None:
                self.next = Merch.begin

                Merch.begin = self
                Merch.end = self
                Merch.count += 1
            else:
                self.next = Merch.begin

                Merch.begin = self
                Merch.count += 1

    def __del__(self):
        super().__del__()