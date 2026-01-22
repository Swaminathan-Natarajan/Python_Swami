

Squares = lambda Arr: Arr*Arr

def main():
    Arr = [10,20,30,40,50]

    Res = list(map(Squares,Arr))

    print("Squares using map is :", Res)


if __name__ == "__main__":
    main()