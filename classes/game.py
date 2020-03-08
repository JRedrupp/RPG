import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.maxhp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def heal(self, amt):
        self.hp += amt
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.hp != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 50

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        if len(hp_string) < 11:
            hp_string = hp_string.rjust(11)

        print("                   __________________________________________________               ")
        print(bcolors.BOLD + self.name + " " + hp_string + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC +"|")

    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 25
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 10

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        if len(hp_string) < 9:
            hp_string = hp_string.rjust(9)

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        if len(mp_string) < 7:
            mp_string = mp_string.rjust(7)


        print("                   _________________________               __________  ")
        print(bcolors.BOLD + self.name + "  " + hp_string +
              " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|     " +
              mp_string + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "| ")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        hp_pct = self.hp / self.maxhp

        if self.mp < spell.cost or (spell.type == "white" and hp_pct > 0.5):
            afford = False
            for spell in self.magic:
                if spell.cost < self.mp:
                    afford = True
                    break
            if afford:
                self.choose_enemy_spell()
            else:
                return False
        else:
            return spell

