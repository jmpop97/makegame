import os
from infos import *
from character_create import *
from action_select import *


# 캐릭터 생성
player_n = 1
# create_character stat입력
# 캐릭터,몬스터 원하는만큼 생성가능
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
    # player =["플레이어1" : string,string]
    # players_info =[player1 : object,object]
    # skills=["공격" : string,string]
    # monsters=["서채연":string,]
    # monsters_info=[monster1 :object]
    actions = action_array_select(
        players, players_info, skills, monsters, monsters_info)

    # 몬스터의 공격
    a_i = 0
    full_HP = 0
    # 선택한후 행동 집어넣기
    # 몬스터 피로 게임 종료보기
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
        break

    # 몬스터 턴

    monster_actions = monster_action_array(
        players, players_info, skills, monsters, monsters_info)
    # 행동후 플레이어 피 확인
    full_HP = 0
    for change_players in players_info:
        full_HP = full_HP + change_players.HP
    if full_HP == 0:
        print("게임 패배")
        break
