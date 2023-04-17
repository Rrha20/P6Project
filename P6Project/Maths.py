LastF = [0, 0, 0]
LastB = [0, 0, 0]


def continuu():
    global LastB, LastF
    opinion = input("Are they the same? 1 => yes. 2 => no.")
    if opinion == "1":
        LastF = findMid()
    if opinion == "2":
        LastB = findMid()
    for i in range(5):
        print(LastF)
        print(LastB)
        opinion = input("Are they the same? 1 => yes. 2 => no.")
        if opinion == "1":
            LastF = findMid()
        if opinion == "2":
            LastB = findMid()
    print(LastF)
    print(LastB)
    print(findMid())


def diff():
    LastB = findMid()


def same():
    LastF = findMid()


def set_Target(col):
    Target = col


def set_Start(col):
    Start = col


def set_LastF(col):
    LastF = col


def set_LastB(col):
    LastB = col


def findMid():
    P1 = LastF
    P2 = LastB
    x = (P1[0] + P2[0]) / 2
    y = (P1[1] + P2[1]) / 2
    z = (P1[2] + P2[2]) / 2
    Current = [x, y, z]
    return [x, y, z]
