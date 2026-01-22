import functools

Mult = lambda No1,No2: No1*No2

def main():
    Arr = [3,2,4,5]

    Res = functools.reduce(Mult,Arr)

    print("Multiplication of all numbers :", Res)


if __name__ == "__main__":
    main()