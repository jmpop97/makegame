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

# play
# try:
action_end = 0
while action_end == 0:
    players_info = [player1, player2]
    monsters_info = [monster1, monster2]
    # 정보
    os.system('cls')
    print("player정보")
    player1.infos()
    player2.infos()
    input("Enter")
    actions = action_array_select(
        players, players_info, skills, monsters, monsters_info)
    a_i = 0
    full_HP = 0
    for change_monsters in monsters_info:
        change_monsters.copys(actions[a_i])
        full_HP = full_HP + change_monsters.HP
        a_i += 1

    # 정보
    os.system('cls')
    print("monster정보")
    monster1.infos()
    monster2.infos()

    input("Enter")
    if full_HP == 0:
        print("게임 승리")
        # raise

    # 몬스터 턴

    monster_actions = monster_action_array(
        players, players_info, skills, monsters, monsters_info)

    full_HP = 0
    for change_players in players_info:
        full_HP = full_HP + change_players.HP
    if full_HP == 0:
        print("게임 패배")
        # raise
# except:
    # print("게임끝")
