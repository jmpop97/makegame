from infos import *

monster_type = {"서채연": [10, 1, 50, 20],
                "노탁근": [5, 100, 10, 100],
                "이세희": [3, 10, 5, 3],
                "이정현": [100, 1, 1, 1],
                "최승원": [10, 1, 5, 3],
                "더미": [0, 0, 0, 0]}


class MonsterInfo(Infos):
    def __init__(self, type):
        monster = monster_type[type]
        self.name = type
        self.HP = monster[0]*30
        self.MP = monster[1]*10
        self.power = monster[2]
        self.mgpower = monster[3]
