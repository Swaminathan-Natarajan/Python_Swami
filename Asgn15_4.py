import functools

Add = lambda No1, No2: No1+No2

def main():
    Arr = [10,20,30,40,50, 21, 31, 41, 51, 60]

    Res = functools.reduce(Add,Arr)

    print("Addition result is :", Res)


if __name__ == "__main__":
    main()