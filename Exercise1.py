# git-exercise-01.py

print ("\nCollaborators: \n 1)Rosie V.\n 2)Henry C.\n")
print ("***THIS IS A SIMPLE PROGRAM THAT ALLOWS YOU TO REVERSE A WORD OR PHRASE AND COUNTS THE FREQUENCY OF A LETTER IN YOUR INPUT.***\n")

# TEAM LEADER:
# implement this function so that it returns copy of string_arg reversed
def reverseWord(string_arg):
	string_arg = string_arg[::-1]
	return string_arg	

# TEAM MEMBER:
# implement this function so that it returns the frequency of query in string_arg
def countFreq(string_arg, query):
	counter = 0
	for i in range(len(string_arg)):
		if string_arg[i] == query:
			counter += 1
	return counter

def main():	
	data = raw_input('Enter your word(s) here: ')
	data_l = raw_input('Enter a letter you would like to know the frequency of: ')
	print '\nYou entered:', "'",data,"'"
	print "\nHere is your word(s) reversed:","'",reverseWord(data),"'"	
	print "\nThe frequency of", "'",data_l,"'", "in","'",data,"'", "is: ",countFreq(data_l, data)
	print '\n\nThank you for using our program!\nHasta Luego(:\n'
if __name__ == "__main__": 
	main()
