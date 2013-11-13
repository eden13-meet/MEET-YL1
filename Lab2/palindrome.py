#1) ask for a raw input string.
#2) check length of string.
#3) divide word into two.
#4) make sure letters in part one correspond to part two.
#5) if they do, return True
#6) if they don't, return false

 #string=raw_input("print")



#def checkifPalindrome(string):
#	length = len(string)
#	int(length)
#	for x in range(string[0], string[length/2]):
#		if x == 







def checkifPalindrome2(string):
	b=string[::-1]
	if string==b:
		return True
	else: return False
string=raw_input("print")
checkifPalindrome2(string)
