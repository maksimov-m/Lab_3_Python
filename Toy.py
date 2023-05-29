from Merch import *

class Toy(Merch):
    def __init__(self, name, producer, material, age_category):
        super().__init__(name, producer)
        self.__material = material
        self.__age_category = age_category
        self.add()

    @property
    def age_category(self):
        return self.__age_category

    @property
    def material(self):
        return self.__material

    def __str__(self):
        return super().__str__() + f"\nMaterial: {self.material}\nAge category: {self.age_category}\n"

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