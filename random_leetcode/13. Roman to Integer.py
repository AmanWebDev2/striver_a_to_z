values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def romanToInt(s: str) -> int:
    total = values.get(s[-1])
    for i in reversed(range(len(s)-1)):
        if values.get(s[i]) < values.get(s[i+1]):
            total -= values.get(s[i])
        else:
            total += values.get(s[i])
    return total

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))