def PrintReverseNumbers(No1):
    Ret = []
    Rev = []
    for i in range(1,No1+1):
        Ret.append(i)
    
        #print("Ret length is:", len(Ret))
    for j in range(len(Ret),0,-1):
        #print("Inside 2nd for")
        Rev.append(j)
        #print("Rev is:", Rev)
    return Rev

    

def main():
    print("Enter the first number :")
    no1 = int(input())

    Res = PrintReverseNumbers(no1)

    print("All numbers reverse are: ", Res)
    


if __name__ == "__main__":
    main()