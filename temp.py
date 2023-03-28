import os


def create_temp(players):
    temp = ""
    i = 1
    for player in players:
        temp = temp+str(i)+"-"+player+" , "
        i += 1
    temp = temp[:-3]+" : "
    return temp


def temp_select(input):
    os.system('cls')
    temp = "플레이어 선택 : "+input[0] + "\n" + \
        "action 선택 : " + input[1] + "\n" + \
        "타겟 선택 : " + input[2] + "\n"
    print(temp)
