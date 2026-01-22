import functools

Max = lambda No1, No2: max(No1,No2)

def main():
    Arr = [10,20,30,40,50, 21, 31, 41, 51, 60]

    Res = functools.reduce(Max,Arr)

    print("Max is :", Res)


if __name__ == "__main__":
    main()