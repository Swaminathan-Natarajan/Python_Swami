import sys
import os
import shutil

def IsWordExist(FileName1, word):
    fobj = open(FileName1, "r")
    content = fobj.read()
    if word.lower() in content.lower():
        return True
    else:
        return False
    


def main():
    Cnt = 0
    fileName1 = sys.argv[1]
    word = sys.argv[2]
    
    if os.path.exists(fileName1):
        Ret = IsWordExist(fileName1, word)

    if Ret == True:
        print(f"{word} exist in the file {fileName1}")
    else:
        print(f"{word} doesnt exist in the file {fileName1}")
    #print("Line by Line printing", Lines)

if __name__ == "__main__":
    main()