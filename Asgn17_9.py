def NoOfDigits(num):
    Cnt = 0

    for i in range(num,0,-1):
        if num > 0:
            
            num = num // 10
            
            Cnt = Cnt + 1
            
    return Cnt

    #while num > 0:
    #    num = num // 10
     #   Cnt = Cnt + 1
    #return Cnt


    
def main():
    print("Enter a number:")
    Num = int(input())
    
    Res = NoOfDigits(Num)

    print("No Of digits of the entered number is:", Res)



if __name__ == "__main__":
    main()