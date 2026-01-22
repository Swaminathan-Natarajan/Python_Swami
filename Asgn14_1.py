
Square = lambda No : No * No


def main():
    print("Enter a Number")
    No = int(input())
    Res = Square(No)

    print("Square using Lambda is:", Res)


if __name__ == "__main__":
    main()

