def find_closest(x,y,z):
    d1 = abs(z-x)
    d2 = abs(z-y)
    if d1 < d2:
        return 1
    elif d2 < d1:
        return 2
    else:
        return 0

print(find_closest(2,7,4))
print(find_closest(2,5,6))