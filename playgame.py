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
# play
action_end = 0
while action_end == 0:
    player1.infos()
    input("")
    actions = action_array_select(players, skills, monsters)
