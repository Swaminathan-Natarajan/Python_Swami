def NaturalNos(No1):
    
    val = 0
    for i in range(1,No1+1):
        val = val+i

    return val


def main():
    print("Enter the number:")
    No1 = int(input())

    Res = NaturalNos(No1)

    print("Sum of natural number entered is :", Res)

if __name__ == "__main__":
    main()