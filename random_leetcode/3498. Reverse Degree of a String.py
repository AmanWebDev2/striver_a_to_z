def reverse_degree(s:str):
	ans = 0
	for i,char in enumerate(s):
		ans += (i+1) * (26 - (ord(char)-ord('a')))
	return ans 