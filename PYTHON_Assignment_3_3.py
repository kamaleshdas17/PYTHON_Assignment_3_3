#Implement a function longestWord() that takes a list of words and returns the longest one.

def longestWord(lst):
	max_len=0
	for val in lst:
		val_len=len(val)
		if val_len > max_len:
			max_len=val_len
			
			
	return max_len,val
		
lst=['abc','def','ghij','klmnop','qrs','tuvwxyz']

max_len,element=longestWord(lst)
print ('Longest element from the given list is:: '+ str(element) + '	length is:: ' + str(max_len))


