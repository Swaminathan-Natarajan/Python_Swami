
Cube = lambda No : No **3


def main():
    print("Enter a Number")
    No = int(input())
    Res = Cube(No)

    print("Cube using Lambda is:", Res)


if __name__ == "__main__":
    main()

