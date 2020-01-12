def palindrome(word):
	for i in range(len(word)-1):
		for j in range(len(word)-1,i,-1):
			if word[i] == word[j] and word[i:j+1] == word[i:j+1][::-1]:
				print("yes")
				print(len(word[i:j+1]))
				break
        
palindrome("cacdebcdcbe")
