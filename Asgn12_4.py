def PrintNumbers(No1):
    Ret = []
    for i in range(1,No1+1):
        Ret.append(i)
    return Ret

    

def main():
    print("Enter the first number :")
    no1 = int(input())

    Res = PrintNumbers(no1)

    print("All numbers till number entered are", Res)
    


if __name__ == "__main__":
    main()