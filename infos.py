import random
from skill import *


class Infos:
    def __init__(self, stat):
        self.name = stat[0]
        self.HP = 20*stat[1]
        self.MP = 10*stat[2]
        self.power = stat[3]
        self.mgpower = stat[4]

    def infos(self):
        print("name : "+self.name)
        print("HP : "+str(self.HP))
        print("MP : "+str(self.MP))
        print("power : "+str(self.power))
        print("mgpower : "+str(self.mgpower))

    def copys(self, obj):
        self.name = obj.name
        self.HP = obj.HP
        self.MP = obj.MP
        self.power = obj.power
        self.mgpower = obj.mgpower

    def attack(self, other):
        damage = int(self.power*random.uniform(0.8, 1.2))
        other.HP = max(other.HP - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.HP == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
