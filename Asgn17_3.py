
def Factorial(No):
    Ans = 1
    for i in range(1,No+1):
        Ans = Ans * i
    return Ans
    
def main():
    print("Enter a number:")
    Num = int(input())
    
    Res = Factorial(Num)
    print("Factorial : ", Res)

if __name__ == "__main__":
    main()