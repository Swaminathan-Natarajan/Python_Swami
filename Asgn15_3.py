

Odd = lambda No: No%2!=0

def main():
    Arr = [10,20,30,40,50, 21, 31, 41, 51, 60]

    Res = list(filter(Odd,Arr))

    print("Filter Odd number result is :", Res)


if __name__ == "__main__":
    main()