
def ArrMin(ArrVal):
    min1 = 0
    min1 = min(ArrVal)

    return min1

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input())
        Arr.append(Val)

    print(Arr)
    Ret = ArrMin(Arr)

    print("Min from Array elements is :", Ret)


if __name__ == "__main__":
    main()
