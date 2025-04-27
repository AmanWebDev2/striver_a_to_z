from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_arr = [0]*26
    
    for char in s:
        hash_arr[ord(char)-ord('a')] += 1

    for char in t:
        hash_arr[ord(char)-ord('a')] -= 1

    for num in hash_arr:
        if num != 0:
            return False
    return True