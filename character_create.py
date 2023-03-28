import os


def create_character(player_n):
    os.system('cls')

    create_character = 0
    while create_character == 0:
        try:
            # 입력하기
            print("캐릭터"+str(player_n)+"를 생성하세요.")
            print("stat의 최대 합 50까지입니다(HP,MP,파워,마법바워)")
            stat = 50
            player_name = input("이름을 입력하세요 : ")
            print("이름은 "+player_name+"입니다.")
            player_HP = int(input("HP의 값을 입력하세요 : "))
            print("HP는 "+str(player_HP)+"입니다.")
            stat -= player_HP
            print("남은 stat : "+str(stat))
            player_MP = int(input("MP의 값을 입력하세요 : "))
            print("MP는 "+str(player_MP)+"입니다.")
            stat -= player_MP
            print("남은 stat : "+str(stat))
            player_power = int(input("파워의 값을 입력하세요 : "))
            print("power는 "+str(player_power)+"입니다.")
            stat -= player_power
            print("남은 stat : "+str(stat))
            player_mgpower = int(input("마법파워의 값을 입력하세요 : "))
            print("mgpower는 "+str(player_mgpower)+"입니다.")
            stat -= player_mgpower
            print("남은 stat : "+str(stat))
            if (stat < 0 or stat > 50 or player_HP < 0 or player_MP < 0 or player_power < 0 or player_mgpower < 0):
                raise

            # 생성
            try:
                check_stat = 0
                while check_stat == 0:
                    os.system('cls')
                    print("HP : "+str(player_HP)+", MP : "+str(player_MP)+", power : " +
                          str(player_power)+", mgpower : "+str(player_mgpower)+", 남은stat : "+str(stat))
                    y_s = input("캐릭터를 확정하시겠습니까? 1-Yes 2-No : ")
                    if y_s == "1":
                        create_character = 1
                        check_stat = 1
                    elif y_s == "2":
                        check_stat = 1
                        raise
            except:
                if (check_stat == 0):
                    print("입력값 오류 다시 작성하세요1")
        except:
            print("입력값 오류 다시 작성하세요2")
    return [player_name, player_HP, player_MP,
            player_power, player_mgpower]
