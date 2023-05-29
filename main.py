from Merch import *
from Product import *
from Toy import *
from MilkProduct import *

# Create obj
d11 = Product("Horse", "Simple green", 25)
d12 = Product("Rabbit", "Simple green", 35)
d13 = Product("Cat", "Simple green", 15)

d21 = MilkProduct("Milk-day", "Today", 1, 2)
d22 = MilkProduct("Chocolate-day", "Today", 3, 1)
d23 = MilkProduct("Cefir-day", "Today", 4, 3)

# Print list before add
Merch.print_mass()
print("----------\n")

# add element
d11.add()
d13.add()

d21.add()
d23.add()

# error accident
d21.add()
d23.add()

# Print past add
Merch.print_mass()
print(f"Mass count {Merch.count}")
print("-------\n")

# del element
d11.__del__()
d21.__del__()

# error accident
d21.__del__()
d21.__del__()

# Print past del
Merch.print_mass()
print(f"Mass count {Merch.count}")
print("------\n")

# add in constructor
d31 = Toy("Robot", "DPA", "plastic", 5)
d32 = Toy("Horse", "DPA", "plastic", 2)



# Print past add constructor
Merch.print_mass()
print(f"Mass count {Merch.count}")