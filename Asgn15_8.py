
Divisible = lambda No1: No1%3==0 and No1%5==0

def main():
    Arr = [10,33,69,55,43,70,25,60,30]

    Res = list(filter(Divisible,Arr))

    print("Numbers Divisible by 3 and 5 are :", Res)


if __name__ == "__main__":
    main()