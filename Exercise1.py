# git-exercise-01.py

print ("***This is an excercise that teaches you to collaborate through Github!***")
print ("Team Members: \n 1)Rosie Vasquez\n 2)Henry Chung")
print ("This is a simple program that allows you to reverse a word(s) and counts the frequecy of a letter in the word(s).")

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
	data = 'guidorossumwashere'
	print ("YOUR WORD IS:", data)	
	print ("REVERSED ==>", reverseWord(data))
	print ("THE FREQUENCY OF s IN", data, "==>", countFreq(data, 's'))

if __name__ == "__main__": 
	main()
