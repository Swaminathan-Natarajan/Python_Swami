
Largest = lambda No1,No2,No3: max(No1,No2,No3)


def main():
    print("Enter a Number")
    No1 = int(input())

    print("Enter a Number")
    No2 = int(input())

    print("Enter a Number")
    No3 = int(input())

    Res = Largest(No1, No2, No3)

    
    print("Largest number is:", Res)
    



if __name__ == "__main__":
    main()

