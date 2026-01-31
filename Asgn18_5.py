import MarvellousPrime
from functools import reduce 



AddPrime = lambda A, B : A + B

def main():
    print("Enter the number of elements")
    Value = int(input())

    Arr = []
    for i in range(Value):
        Val = int(input())
        Arr.append(Val)

    print(Arr)
    
    ChkPrime = MarvellousPrime.ChkPrime(Arr)
    print("List of prime numbers is:", ChkPrime)
    
    Ret = reduce(AddPrime, ChkPrime)

    print("Addition of Prime is :", Ret)


if __name__ == "__main__":
    main()
