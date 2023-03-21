def palindrome(pList):
	i = len(pList)
	for j in range(i // 2):
		if pList[j] != pList[i-j-1]:
			return False
	return True
