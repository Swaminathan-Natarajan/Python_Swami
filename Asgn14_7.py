
DivisibleBy5 = lambda No1: No1%5==0


def main():
    print("Enter a Number")
    No1 = int(input())

    Res = DivisibleBy5(No1)

    if Res == True:
        print("Number is Divisible by 5: ", No1)
    else:
        print("Number is not Divisible by 5:", No1)


if __name__ == "__main__":
    main()

