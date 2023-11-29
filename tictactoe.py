# Den bästa koden för X O spelet
tavla = [' ' for x in range(10)]

# Alla funktioner
def infoga(bok,punkt):
    tavla[punkt] = bok

def utrymme(punkt):
    return tavla[punkt] == ' '

# Funktionen för tavlan eller brädan med print
def tavlakod(tavla):
    print('   |   |   ')
    print(' ' + tavla[1] + ' | ' + tavla[2] + ' | ' + tavla[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + tavla[4] + ' | ' + tavla[5] + ' | ' + tavla[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + tavla[7] + ' | ' + tavla[8] + ' | ' + tavla[9])
    print('   |   |   ')

def helatavlan(tavla):
    if tavla.count(' ') > 1:
        return False
    else:
        return True

def vinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

# Funktionen för instruktioner
def spelare1():
    run = True
    while run:
        flytta = int(input("Skriv ett nummer mellan 1 och 9 för att sätta X \n"))
        try:
            flytta = int(flytta)
            if flytta > 0 and flytta < 10:
                if utrymme(flytta):
                    run = False
                    infoga('X' , flytta)
                else:
                    print('Förlåt, nummret är upptaget')
            else:
                print('Välj ett nummer mellan 1 och 9')

        except:
            print('Skriv ett nummer')

# Funktion för datorns tur att spela
def datormove():
    mojligutdrag = [x for x , bok in enumerate(tavla) if bok == ' ' and x != 0  ]
    flytta = 0

    for let in ['O' , 'X']:
        for i in mojligutdrag:
            tavlakopiera = tavla[:]
            tavlakopiera[i] = let
            if vinnare(tavlakopiera, let):
                flytta = i
                return flytta

    vinkelOp = []
    for i in mojligutdrag:
        if i in [1 , 3 , 7 , 9]:
            vinkelOp.append(i)

    if len(vinkelOp) > 0:
        flytta = valrandom(vinkelOp)
        return flytta

    if 5 in mojligutdrag:
        flytta = 5
        return flytta

    edgesOpen = []
    for i in mojligutdrag:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        flytta = valrandom(edgesOpen)
        return flytta

# radnom nummer
def valrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Välkommen till spelet")
    tavlakod(tavla)

# While loop om man vinner eller inte
    while not(helatavlan(tavla)):
        if not(vinnare(tavla , 'O')):
            spelare1()
            tavlakod(tavla)
        else:
            print("Du förlorade!")
            break

        if not(vinnare(tavla , 'X')):
            flytta = datormove()
            if flytta == 0:
                print(" ")
            else:
                infoga('O' , flytta)
                print('Datorn placerar ett o på en position' , flytta , ':')
                tavlakod(tavla)
        else:
            print("Du vann!")
            break



# Om ingen vinner så händer det
    if helatavlan(tavla):
        print("Oavgjort spel")

# While loopen för att fråga varje gång
while True:
    x = input("Vill du spela? tryck på J för Ja och N för Nej (J/N)\n").lower()
    if x.lower() == 'j':
        tavla = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
