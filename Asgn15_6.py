import functools

Min = lambda No1, No2: min(No1,No2)

def main():
    Arr = [1,10,20,30,40,50, 21, 31, 41, 51, 60]

    Res = functools.reduce(Min,Arr)

    print("Min is :", Res)


if __name__ == "__main__":
    main()