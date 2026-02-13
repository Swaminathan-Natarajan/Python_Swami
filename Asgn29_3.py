import sys
import os

def DisplayContents(DirName,Name):
    #print("File Name:", FileName)
    if os.path.exists(DirName) == False:
        print("Dir is not Valid")
        return
     
    

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for Fname in FileName:
            
            if Fname == Name:
                fobj = open(Name,"rb")
                
                fobj1 = open("CopyText.txt", "wb")
                fobj1.write(fobj.read())


def main():

    if(len(sys.argv) != 2 ):
        print("Invalid number of args")
        return

    currentDir = os.getcwd()
    DisplayContents(currentDir, sys.argv[1])



if __name__ == "__main__":
    main()