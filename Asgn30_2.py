import sys
import os

def CountWords(FileName):
    cnt = 0
    fobj = open(FileName, "r")
    content = fobj.read()
    words = content.split()
    cnt = len(words)
    return cnt


def main():
    Cnt = 0
    fileName = sys.argv[1]
    print("File path :", os.path.exists(fileName))
    if os.path.exists(fileName):
        Cnt = CountWords(sys.argv[1])
    print("Word count in the file are:", Cnt)

if __name__ == "__main__":
    main()