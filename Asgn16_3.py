def Add(No1, No2):
    return No1 + No2

def main():
    print("Enter a Number:")
    No1 = int(input())

    print("Enter a Number:")
    No2 = int(input())

    Res = Add(No1, No2)

    print("Additon is :", Res)

if __name__ == "__main__":
    main()