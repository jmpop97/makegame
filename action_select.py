from temp import *
from infos import *
from monster import *


def action_select(players, skills, monsters):
    select_action = 0

    while select_action == 0:
        # 플레이어 선택
        select_erro = 0
        actions_name = ["", "", ""]
        while select_erro == 0:
            try:
                temp_select(actions_name)
                temp = create_temp(players)
                print("player선택")
                get_action = input(temp)
                if 0 < int(get_action) and int(get_action) <= int(len(players)):
                    actions_name[0] = players[int(get_action)-1]
                    select_erro = 1
            except:
                pass
        # 행동선택
        select_erro = 0
        while select_erro == 0:
            try:
                temp_select(actions_name)
                temp = create_temp(skills)
                print("player선택")
                get_action = input(temp)
                if 0 < int(get_action) and int(get_action) <= 2:
                    actions_name[1] = skills[int(get_action)-1]
                    select_erro = 1
            except:
                pass
        # 대상 선택
        select_erro = 0
        while select_erro == 0:
            try:
                temp_select(actions_name)
                temp = create_temp(monsters)
                print("공격대상 선택")
                get_action = input(temp)
                if 0 < int(get_action) and int(get_action) <= int(len(monsters)):
                    actions_name[2] = monsters[int(get_action)-1]
                    select_erro = 1
            except:
                pass

        # 확인
        select_erro = 0
        while select_erro == 0:
            try:
                temp_select(actions_name)
                get_action = input("행동 선택 1-Yes , 2-No : ")
                if get_action == "1":
                    select_erro = 1
                    select_action = 1
                    # key_action = {actions_name[0]: actions_name[1:3]}
                elif get_action == "2":
                    select_erro = 1
            except:
                pass

    return actions_name

# 행동dictionary생성


def action_array_select(players, players_info, skills, monsters, monsters_info):

    turn_end = 0
    # 더미 데이터
    while turn_end == 0:
        i = 0
        dmonsters_info = []
        for monster in monsters_info:
            locals()["d"+monsters[i]] = MonsterInfo("더미")
            locals()["d"+monsters[i]].copys(monster)

            dmonsters_info = dmonsters_info + \
                [locals()["d"+monsters[i]]]

            i += 1
        dplayers = players
        select_action = 0
        while select_action == 0:
            action = action_select(dplayers, skills, monsters)
            players_info[players.index(action[0])].attack(
                dmonsters_info[monsters.index(action[2])])

            # 행동된 플레이어 삭제제
            del dplayers[dplayers.index(action[0])]
            select_erro = 0
            while select_erro == 0:
                try:
                    print(action)
                    get_action = input("1-다음행동 , 2-초기화 , 3-다음턴 : ")
                    # 다음행동
                    if get_action == "1":
                        select_erro = 1
                    # 초기화
                    elif get_action == "2":
                        select_erro = 1
                        select_action = 1
                    # 다음턴
                    elif get_action == "3":
                        select_erro = 1
                        select_action = 1
                        turn_end = 1

                except:
                    pass
        return dmonsters_info
