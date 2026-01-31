def DivisibleBy5(Num):
    return Num % 5 == 0
        
    




def main():
    print("Enter a Number:")
    Num = int(input())

    Res = DivisibleBy5(Num)

    if Res == True:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()