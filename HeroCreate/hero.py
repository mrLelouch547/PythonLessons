class Hero():
    Hero_Types = ("Warrior","Mage","Priest","Rogue")
    def __init__(self, name, gender,gameClass):
        self.name = name
        self.gender = gender
        self.gameclass = gameClass
        self.maingun = ""
        self.extraItem = []
    def print(self):
        return f"User({self.name}, {self.gender}, {self.gameclass})"
    def add_weapon(self):
        pass
    def add_item(self):
        pass
    
try:
    hero1 = Hero(str(input("Type hero name: ")),str( input("Type hero gender: ")),int(input("Type hero class: ") ))
    hero1.print()
except:
    (ValueError)

    