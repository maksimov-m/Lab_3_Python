class Merch(object):
    begin = None
    end = None
    count = 0

    def __init__(self, name, producer):
        self.__name = name
        self.__producer = producer
        self.next = None

    @staticmethod
    def print_mass() -> None:
        tmp = Merch.begin
        if tmp == None:
            print("List Empty")
            return
        while tmp != None:
            print(tmp)
            print()
            tmp = tmp.next

    def el_in_mass(self, el) -> bool:
        tmp = Merch.begin
        if tmp == None:
            return False
        while tmp != None:
            if tmp == el:
                return True
            tmp = tmp.next
        return False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def producer(self) -> str:
        return self.__producer

    def __str__(self) -> str:
        return f"Name : {self.name}\n" \
               f"Producer: {self.producer}"

    def __del__(self):
        if self == Merch.begin:
            Merch.begin = self.next
            Merch.count -= 1
        else:
            tmp = Merch.begin
            while tmp != None and tmp.next != self:
                tmp = tmp.next
            if tmp != None:
                tmp.next = self.next
                Merch.count -= 1



