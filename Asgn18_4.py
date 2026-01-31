
def Freq(ArrVal, num):
    cnt = 0
    val = 0
    for i in range(len(ArrVal)):
        if ArrVal[i] == num:
            cnt = cnt +1

    return cnt

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input())
        Arr.append(Val)

    print(Arr)
    print("Enter number to find frequency :")
    freq = int(input())
    
    Ret = Freq(Arr, freq)

    print("Frequency :", Ret)


if __name__ == "__main__":
    main()
