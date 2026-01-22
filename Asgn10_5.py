def OddNum(No1):
    
    val = []
    for i in range(1,No1+1,2):
        val.append(i)

    return val


def main():
    print("Enter the number:")
    No1 = int(input())

    Res = OddNum(No1)

    print("Odd number till the number entered is :", Res)

if __name__ == "__main__":
    main()