class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl

char_one = Character("Areanne", 200, 100, 50, 10)
print(f"Your character's name is {char_one.name} and HP is {char_one.hp}.")