from functools import reduce

def filterEven(A):
    if A % 2 == 0:
        return A
    
EvenSquare = lambda A : A ** 2

AddAll = lambda A, B : A + B

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input(f"Enter {Value} numbers :"))
        Arr.append(Val)

    print(Arr)
    
    FArr = list(filter(filterEven,Arr))

    print("Filter list Even numbers are :", FArr)

    MArr = list(map(EvenSquare, FArr))

    print("Map list after square is:", MArr)

    RArr = reduce(AddAll, MArr)

    print("Reduce value is Addition of all list val:", RArr)

    


if __name__ == "__main__":
    main()
