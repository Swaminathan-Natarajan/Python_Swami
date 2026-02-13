# Replace all Extension1 by Extension2
import sys
import os
import time




def ReplaceFileExtensions(DirName, Extension1, Extension2):
    Border = "*"*55
    Timestamp = time.ctime()
    #LogFileName = "Assignment31-1%s.log"%(Timestamp)
    fobj = open("Marvellous1","w")
    fobj.write(Border + "\n")
    fobj.write(f"----------Files with Extension Replacement from {Extension1} By {Extension2} ------------"+ "\n")

    if Extension1 == Extension2:
        print("Both the extensions are the same")
        return

    if(os.path.isdir(DirName) == False):
        print("Not a Valid Dir")
        return
    
    if(os.path.exists(DirName) == False):
        print("Dir with this name does not exist")
        return
    
    convertedList = []
    FileExt1 = []
    FileExt2 = []
    #print("Extension passed is:", Extension)
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            
            if os.path.splitext(fname)[1].lower() == Extension1:
                #print("Inside if")
                FileExt1.append(fname)
                #print("FileExt1 is:", FileExt1)
            if os.path.splitext(fname)[1].lower() == Extension2:
                FileExt2.append(fname)
                #print("FileExt2 is:", FileExt2)
                        

    for i in FileExt1:
        newName = i.replace(Extension1,Extension2)
        convertedList.append(newName)


    print("File Extension 1 is :", FileExt1)
    print("File Extension 2 is :", FileExt2)
    print("Converted list is :", convertedList)
    

    fobj.write(Border+"\n")
    fobj.write("----------------- Automation Report Start -----------------"+ "\n")

    fobj.write("Converted List is :" + "\n")
    for i in convertedList:
        fobj.write(i+"\n")
    
    fobj.write("This log file is created at:" + Timestamp + "\n")
    fobj.write("----------------- Automation Report Ends -----------------"+ "\n")
    
    fobj.write(Border)
    fobj.close()		

def main():

    Border = "*"*50
    print(Border)
    print("------------Marvellous Directory Automation-----------------")
    print(Border)
    if(len(sys.argv) != 4 ):
        print("Invalid number of args, please pass 3 arguments: Directory name and File Extension")
        print("Arguments are Directory Name, 1st extension, 2nd extension")
        return


    ReplaceFileExtensions(sys.argv[1], sys.argv[2],sys.argv[3])

    print(Border)
    print("------------Marvellous Directory Automation-----------")
    print(Border)


if __name__ == "__main__":
    main()