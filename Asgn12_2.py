def Factors(No):
    Val = []
    for i in range(1,No+1):
        if No%i == 0:
            Val.append(i)
            

    return Val

    

def main():
    print("Enter the number :")
    no = int(input())

    Res = Factors(no)
    print("Factorial of the given number is:", Res)


if __name__ == "__main__":
    main()