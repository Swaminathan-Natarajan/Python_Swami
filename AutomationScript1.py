import sys


def main():
    Border = "-"*50
    print(Border)
    print("----------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform _______________ ")
            print("This is an automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ______________ ")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : ______")
            print("Argument2 : ______")
        else:
            print("Use the given flags as:")
            print("--u is used to display the Usage")
            print("--h is used to display Help")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as:")
        print("--u is used to display the Usage")
        print("--h is used to display Help")

    print(Border)
    print("------- Thank You for using our Script ------------")
    print("----------- Marvellous Infosystems ----------------")
    print(Border)


if __name__ == "__main__":
    main()