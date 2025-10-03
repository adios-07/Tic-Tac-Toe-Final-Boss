import random

#Easy Difficulty
def BotPick_Easy(GS):
    che = random.randint(0,8)
    while(GS[che] != 0): che = random.randint(0,8)
    return che


#Medium Difficulty
def BotPick_Medium(GS):
    winCond = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    sm = []
    for i in winCond:
        sum = 0
        for j in i:
            sum+=GS[j-1]
        sm.append(sum)

    #Bot finds winning move
    try:
        ind = sm.index(10)
        for j in winCond[ind]:
            if(GS[j-1] == 0):
                return j-1
    except:
        pass

    #Bot finds opp. winning move
    try:
        ind = sm.index(2)
        for j in winCond[ind]:
            if(GS[j-1] == 0):
                #GS[j-1] = 5
                return j-1
    except:
        pass

    #Random Picking
    che = random.randint(0,8)
    while(GS[che] != 0): che = random.randint(0,8)
    return che


#Hard Difficulty
def P_Actions(GS):
    Acn = []
    for i in range(len(GS)):
        if(GS[i] == 0): Acn.append(i) 
    return Acn

def N_GS(GS, a, Val):
    NxtGS = []
    for i in range(len(GS)):
        if(i == a): NxtGS.append(Val)
        else: NxtGS.append(GS[i])
    return NxtGS

def MiniMax(GS, is_Bot_Maxm):
    winCond = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #Terminal State - Victory/Loss
    for i in winCond:
        sum = 0
        for j in i:
            sum += GS[j-1]
        if(sum == 15): return +1
        if(sum == 3): return -1
    
    #Terminal State - Draw
    isDraw = True
    for i in GS:
        if(i == 0):
            isDraw = False
            break
    if(isDraw):
        return 0
    
    #Game Continues
    if(is_Bot_Maxm):
        value = -1000
        for a in P_Actions(GS):
            value = max(value, MiniMax(N_GS(GS, a, 5), False))
        return value
    else:
        value = 1000
        for a in P_Actions(GS):
            value = min(value, MiniMax(N_GS(GS, a, 1), True))
        return value
    
    return None

def BotPick_Hard(GS):
    b_Move = None
    b_Val = -1000
    for a in P_Actions(GS):
        n_val = MiniMax(N_GS(GS, a, 5), False)
        if(n_val > b_Val):
            b_Val = n_val
            b_Move = a

    return (b_Move)