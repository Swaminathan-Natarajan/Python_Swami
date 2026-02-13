import sys
import os

def CountLines(FileName):
    cnt = 0
    fobj = open(FileName, "r")
    content = fobj.readlines()
    cnt = len(content)
    
    return cnt


def main():
    Cnt = 0
    fileName = sys.argv[1]
    print("File path :", os.path.exists(fileName))
    if os.path.exists(fileName):
        Cnt = CountLines(sys.argv[1])
    print("Line count in the file are:", Cnt)

if __name__ == "__main__":
    main()