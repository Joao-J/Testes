
#Entrada de dados (a 10 9 13 7 b 12 3 10 14 c 8 10 12 10 d 15 8 14 9)
#Saida dos dados ( a -> (10, 9, 13, 7) -> 9.75 b -> (12, 3, 10, 14) -> 9.75 c -> (8, 10, 12, 10) -> 10.0 d -> (15, 8, 14) -> 12.33)

Entrada_Dados = "a 10 9 13 7 b 12 3 10 14 c 8 10 12 10 d 15 8 14 9"
NUM = ""
COUNT = 0
GPA = 0.0
DATA_PRINT = []
GROUP = []
CARACT = ""

for C in list(Entrada_Dados):
    try:
        if(int(C) > -1):
            NUM += str(C)
    except:
        if(C != " "):
            if (COUNT > 0):
                GPA /= float(COUNT)
                DATA_PRINT.append(CARACT + " -> " + str(GROUP)+ " -> " +str(GPA))
                COUNT = 0
                GPA = 0.0
                GROUP=[]
            CARACT = C
        elif (C == " " and len(NUM) > 0):
            GPA += float(NUM)
            GROUP.append(int(NUM))
            COUNT += 1
            NUM = ""
            
GPA /= float(COUNT)
DATA_PRINT.append(CARACT + str(GROUP)+ str(GPA))

for i in DATA_PRINT:
    print(str.replace(str(i).replace("[","("),"]",")"))
