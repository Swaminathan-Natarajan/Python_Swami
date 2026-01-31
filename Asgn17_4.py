
def AddFactors(No):
    Ans = 0
    for i in range(1,No):
        if No%i==0:
            Ans = Ans + i
            
    return Ans
    
def main():
    print("Enter a number:")
    Num = int(input())
    
    Res = AddFactors(Num)
    print("Addition on Factors : ", Res)

if __name__ == "__main__":
    main()