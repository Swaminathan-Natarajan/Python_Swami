import hashlib #module to use md5 for checksum algorithm
import os
import sys


		
	
def FindOccurances(FileName, Text):

	cnt = 0
	fobj = open(FileName,"r")
	content = fobj.read().lower()
	cnt = content.count(Text.lower())

	return cnt

			

def main():

	if(len(sys.argv) != 3 ):
		print("Invalid number of args")
		return
    	    
	Count = FindOccurances(sys.argv[1], sys.argv[2])
	
	print(f"Occurances of the word {sys.argv[2]} is {Count}")
	

if __name__ == "__main__":
	main()