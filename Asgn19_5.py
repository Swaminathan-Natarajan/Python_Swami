from functools import reduce

def filterPrime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2,n+1):
       
        if (n % i == 0):
            break
        else:
            return n
        
    
Mult2 = lambda A : A * 2

MaxNum = lambda A, B : max(A,B)

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input(f"Enter {Value} numbers :"))
        Arr.append(Val)

    print(Arr)
    
    FArr = list(filter(filterPrime,Arr))

    print("Filter list Prime numbers are :", FArr)

    MArr = list(map(Mult2, FArr))

    print("Map list after Mult by 2 is:", MArr)

    RArr = reduce(MaxNum, MArr)

    print("Reduce is MAX value:", RArr)

    


if __name__ == "__main__":
    main()
