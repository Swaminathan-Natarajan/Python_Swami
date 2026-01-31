
def ArrAddition(ArrVal):
    Sum = 0
    for i in range(len(ArrVal)):
        Sum = Sum + ArrVal[i]

    return Sum


def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input())
        Arr.append(Val)

    print(Arr)
    Ret = ArrAddition(Arr)

    print("Sum of Array elements are :", Ret)


if __name__ == "__main__":
    main()
