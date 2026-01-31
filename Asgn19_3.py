from functools import reduce

def filterNums(A):
    if A >= 70 and A <= 90:
        return A
    
Add10 = lambda A : A + 10

MultAll = lambda A, B : A * B

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input(f"Enter {Value} numbers :"))
        Arr.append(Val)

    print(Arr)
    
    FArr = list(filter(filterNums,Arr))

    print("Filter list is :", FArr)

    MArr = list(map(Add10, FArr))

    print("Map list after adding 10 is:", MArr)

    RArr = reduce(MultAll, MArr)

    print("Reduce value is multiplication of all list val:", RArr)

    


if __name__ == "__main__":
    main()
