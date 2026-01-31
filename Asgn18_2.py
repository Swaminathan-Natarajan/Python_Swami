
def ArrMax(ArrVal):
    max1 = 0
    max1 = max(ArrVal)

    return max1

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input())
        Arr.append(Val)

    print(Arr)
    Ret = ArrMax(Arr)

    print("Max from Array elements is :", Ret)


if __name__ == "__main__":
    main()
