from infos import *

monster_type = {"서채연": [10, 1, 50, 20],
                "노탁근": [5, 100, 1, 50],
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


def monster_action_array(players, players_info, skills, monsters, monsters_info):
    for monster in monsters_info:
        if monster.name == "서채연":
            player_HP = 0
            for player in players_info:
                if player_HP < player.HP:
                    player_HP = player.HP
                    max_HP_p = player
            monster.attack(max_HP_p)

        elif monster.name == "노탁근":
            player_mgpower = 0
            for player in players_info:
                if player_mgpower < player.mgpower:
                    player_mgpower = player.mgpower
                    max_mgpower_p = player
            monster.mga1(max_mgpower_p)

        elif monster.name == "이정현":
            for player in players_info:
                monster.attack(player)
