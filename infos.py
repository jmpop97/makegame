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
        die(other)

    def mga1(self, other):

        if self.MP < 10:
            self.MP = 0
            print(f"마법이 취소되었습니다. -{self.MP}MP")
        else:
            self.MP -= 10
            damage = int(self.mgpower*1.5)
            other.HP = max(other.HP - damage, 0)
            print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
            die(other)

    def mgh1(self):
        if self.MP < 10:
            self.MP = 0
            print(f"마법이 취소되었습니다. -{self.MP}MP")
        else:
            self.MP -= 10
            self.HP += self.mgpower*10


def die(obj):
    if obj.HP == 0:
        obj.HP = 0
        obj.MP = 0
        obj.power = 0
        obj.mgpower = 0
        print(f"{obj.name}이(가) 쓰러졌습니다.")
