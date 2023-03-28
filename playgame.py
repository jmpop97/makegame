import os
from infos import *
from character_create import *
from action_select import *


# 캐릭터 생성
player_n = 1
globals()["player_info{}".format(player_n)] = create_character(player_n)
globals()["player{}".format(player_n)] = Infos(
    globals()["player_info{}".format(player_n)])
player_n = 2
globals()["player_info{}".format(player_n)] = create_character(player_n)
globals()["player{}".format(player_n)] = Infos(
    globals()["player_info{}".format(player_n)])
player1.infos()
player2.infos()

players = ["player1", "player2"]
skills = ["공격", "마법"]
monsters = ["monster1", "monster2"]

monster1 = MonsterInfo("서채연")
monster2 = MonsterInfo("이정현")
players_info = [player1, player2]
monsters_info = [monster1, monster2]
# play
action_end = 0
while action_end == 0:
    monster1.infos()
    input("")

    actions = action_array_select(
        players, players_info, skills, monsters, monsters_info)
    a_i = 0
    for change_monsters in monsters_info:
        change_monsters.copys(actions[a_i])
        a_i += 1
1
