import sys
import os

def CheckFileName(DirName,Name):
    #print("File Name:", FileName)
    if os.path.exists(DirName) == False:
        print("Dir is not Valid")
        return
     

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for Fname in FileName:
            
            if Fname == Name:
                print(f"{Fname} exists in {DirName}")

def main():

    if(len(sys.argv) != 2 ):
        print("Invalid number of args")
        return

    currentDir = os.getcwd()
    CheckFileName(currentDir, sys.argv[1])



if __name__ == "__main__":
    main()