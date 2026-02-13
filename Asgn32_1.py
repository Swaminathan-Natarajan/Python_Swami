import hashlib #module to use md5 for checksum algorithm
import os
import sys
import time

def CalculateCheckSum(FileName):
	
	fobj = open(FileName,"rb")
	
	hobj = hashlib.md5()
	
	Buffer = fobj.read(1000)

	while(len(Buffer) > 0):
		hobj.update(Buffer)
		Buffer = fobj.read(1024)
	
	fobj.close()
	
	return hobj.hexdigest()	

def DisplayChecksum(DirectoryName):
	Border = "*"*55
	Timestamp = time.ctime()
	fobj = open("DrectoryCheckSum.txt","w")
	fobj.write(Border + "\n")
	
	
	Ret = False
	Ret = os.path.exists(DirectoryName)
	
	if(Ret == False):
		print("There is no such Dir")
		return

	Ret = os.path.isdir(DirectoryName)
	if(Ret == False):
		print("It is not a Dir")
		return	
	
	for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
		for fName in FileName:
			fName = os.path.join(FolderName,fName)
			CheckSum = CalculateCheckSum(fName)

			print(f"File Name : {fName} Checksum : {CheckSum} \n")
			fobj.write(f"File Name : {fName} Checksum : {CheckSum} \n")
    
    	

			

def main():
	Border = "*"*50
	print(Border)
	print("------------Marvellous Directory Automation-----------------")
	print(Border)
	if(len(sys.argv) != 2 ):
		print("Invalid number of args")
		return

	DisplayChecksum(sys.argv[1])
	
	print(Border)
	print("------------Marvellous Directory Automation-----------")
	print(Border)

if __name__ == "__main__":
	main()