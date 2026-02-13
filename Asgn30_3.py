import sys
import os

def PrintLines(FileName):
    cnt = 0
    fobj = open(FileName, "r")
    content = fobj.readlines()
    for line in content:
        print(line.strip())
    


def main():
    Cnt = 0
    fileName = sys.argv[1]
    print("File path :", os.path.exists(fileName))
    if os.path.exists(fileName):
        PrintLines(sys.argv[1])
    #print("Line by Line printing", Lines)

if __name__ == "__main__":
    main()