import sys
import os
import shutil

def CopyContents(FileName1, FileName2):
    shutil.copy2(FileName1, FileName2)
    


def main():
    Cnt = 0
    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]
    if not os.path.exists(fileName2):
        open(fileName2,"wb")
        if os.path.exists(fileName2):
            print("2nd file created", fileName2)
    if os.path.exists(fileName1):
        CopyContents(fileName1, fileName2)
    #print("Line by Line printing", Lines)

if __name__ == "__main__":
    main()