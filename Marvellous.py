PI = 3.14
print("Inside Module : ",__name__)
def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Sub(No1, No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Mult(No1,No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def Div(No1, No2):
    Ans = 0
    try:
        Ans = No1 / No2
    except ZeroDivisionError as obj:
        print(obj)
    return Ans


