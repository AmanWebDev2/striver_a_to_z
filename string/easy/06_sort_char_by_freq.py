from collections import Counter

"""
Time Complexity: O(n + k log k)
Space Complexity: O(n)
"""
def frequencySort(s: str) -> str:
    freq = Counter(s)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    new_str = ""
    for char,count in sorted_freq:
        new_str += char * count
    return new_str

print(frequencySort("tree"))