class Item:
    def __init__(self,name):
        self.name = name
        self.durability = 100

class Weapon(Item):
    def __init__(self, name, attack):
        super().__init__(name)
        self.attack = attack
    
    def print_nameitem(self):
        print(self.name)
    def print_nameweapon(self):
        print(self.name)
try:
    item1 = Item(str(input("Type item name: ")))
    weapon1 = Weapon(str(input("Type weapon name: ")))
except:
    (ValueError)
