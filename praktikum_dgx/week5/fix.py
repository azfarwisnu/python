import random 
import math
 
def acakkesempatan(a, b):
    pilihan = ['0', '1', '2']
    probability = ['0', '1', '2']
 
    for i in range(0, a - 1):
        f = []
        for j in range(0, len(pilihan)):
            x = pilihan[j]
            for k in range(0,3):
                y = x + probability[k]
                f.append(y)
        pilihan = f
        
    for key in b:
        for i in range(0, len(pilihan)):
            b[key][pilihan[i]] = 0.1
            
    return b
 
 
 
def scoreterbaru(usr, bot):
    global score_user
    global score_bot
 
    if score_user <= 20 or score_bot <= 20:
 
        user_menang = False
        bot_win = False
 
        if usr == 0 and bot == 1: 
            score_user += 1
            user_menang = True
        elif usr == 1 and bot == 0:
            score_bot += 1
            bot_win = True
        elif usr == 1 and bot == 2: 
            score_user += 1
            user_menang = True
        elif usr == 2 and bot == 1:
            score_bot += 1
            bot_win = True
        elif usr == 2 and bot == 0: 
            score_user += 1
            user_menang = True
        elif usr == 0 and bot == 2:
            score_bot += 1
            bot_win = True
        
    scoreboard_usr = "| User : " + str(score_user).rjust(2,"0") + "|" + ("x"*score_user).ljust(20," ") + "|"
    scoreboard_bot = "| Bot  : " + str(score_bot).rjust(2,"0") + "|"+ ("x"*score_bot).ljust(20," ") + "|"
 
    if user_menang == True and score_user < 20:
        scoreboard_usr += " +1"
    elif bot_win == True and score_bot < 20 :
        scoreboard_bot += " +1"
    elif score_user == 20:
        scoreboard_usr += " WIN!"
        scoreboard_bot += " LOSE!"
    elif score_bot == 20:
        scoreboard_usr += " LOSE"
        scoreboard_bot += " WIN!"
 
 
    print("")
    print("")
    print("Score Berjalan : ")
    print(scoreboard_usr)
    print(scoreboard_bot)
    print("")
 
def mulai_game():
    
 
    print("Gunting BATU KERTAS")
    print("Dapatkan 20 POINTS kalahkan BOT \n")

    print("1.Gunting")
    print("2.Batu")
    print('3.Kertas')

    numberOfChoices = 2
    status = True
    pilihanUser = []
 
    while status == True:
        if score_user == 20 or score_bot == 20:
            break
        print("Masukkan pilihan anda Batu/Gunting/Kertas: ", end = ' ')
        
        try:
            usr_input = str(input())
        except Exception:
            print()
            print("[!]  Silahkan pilih Batu/Gunting/Kertas ")
            continue
 
        if usr_input.lower() == "batu":
            r = 0
        elif usr_input.lower() == "gunting":
            r = 1
        elif usr_input.lower() == "kertas":
            r = 2
        else:
            print("[!]  Silahkan pilih Batu/Gunting/Kertas ")
            continue
        
        pilihanUser.append(r)
        
        follupPilihanUser = pilihanUser[0:len(pilihanUser) - 1]
        b = dict()
        b[0] = dict()
        b[1] = dict()
        b[2] = dict()
 
        if numberOfChoices >= len(follupPilihanUser):
            pilihanBot = random.randint(0, 2)
            dijawabot = ''
            dijawabuser = ''
            if pilihanBot == 0:
                dijawabot = 'Batu'
            elif pilihanBot == 1:
                dijawabot = 'Gunting'
            elif pilihanBot == 2:
                dijawabot = 'Kertas'
            
            if r == 0:
                dijawabuser = 'Batu'
            elif r == 1:
                dijawabuser = 'Gunting'
            elif r == 2:
                dijawabuser = 'Kertas'
 
            scoreterbaru(r,pilihanBot)
 
        elif numberOfChoices < len(follupPilihanUser):
            b = acakkesempatan(numberOfChoices, b)
            c = math.pow(3, numberOfChoices)
            normalizer = c * 0.1
 
            for i in range(0, len(follupPilihanUser)):
                if i + numberOfChoices < len(follupPilihanUser):
                    key1 = follupPilihanUser[i]
                    key2 = ''.join(str(x) for x in follupPilihanUser[i:i + numberOfChoices])
 
                    lastVal = b[key1][key2]
                    b[key1][key2]
 
            for key in b:
                for i in b[key]:
                    if b[key][i] != 0.1:
                        lastVal = b[key][i]
                        base = follupPilihanUser[0 + numberOfChoices].count(key)
                        b[key][i] = lastVal / (base + normalizer)
 
            aInputTerakhir = ''.join(str(x) for x in follupPilihanUser[len(follupPilihanUser) - numberOfChoices:])
 
            probabilitasResp = []
 
            for key in b:
                pKey = round(follupPilihanUser.count(key), 3) / len(follupPilihanUser)
                pKey = round(pKey, 3)
 
                pengkondisianKey = b[key][aInputTerakhir]
                val = pengkondisianKey * pKey
                probabilitasResp.append(val)
 
            normalSum = 0
 
            for i in range(0, len(probabilitasResp)):
                normalSum = normalSum + probabilitasResp[i]
 
            finalResp = []
 
            for i in range(0, len(probabilitasResp)):
                finalResp.append(probabilitasResp[i]/normalSum)
 
            utilResp = []
            for i in range(0, len(finalResp)):
                if i == 0:
                    utilResp.append(finalResp[1] - finalResp[2])
                elif i == 1:
                    utilResp.append(finalResp[2] - finalResp[0])
                elif i == 2:
                    utilResp.append(finalResp[0] - finalResp[1])
 
            pilihanBot = utilResp.index(max(utilResp))
 
            dijawabot = ''
            dijawabuser = ''
            if pilihanBot == 0:
                dijawabot = 'Batu'
            elif pilihanBot == 1:
                dijawabot = 'Gunting'
            elif pilihanBot == 2:
                dijawabot = 'Kertas'
 
            if r == 0:
                dijawabuser = 'Batu'
            elif r == 1:
                dijawabuser = 'Gunting'
            elif r == 2:
                dijawabuser = 'Kertas'
            
            scoreterbaru(r,pilihanBot)
 
        print("User : " + str(dijawabuser))
        print("Bot  : " + str(dijawabot))
 
score_user = 0
score_bot = 0
mulai_game()