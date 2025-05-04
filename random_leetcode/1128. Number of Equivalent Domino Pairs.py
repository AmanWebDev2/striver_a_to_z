from collections import defaultdict
def numEquivDominoPairs(dominoes: list[list[int]]) -> int:
    count = 0
    mpp = defaultdict(int)
    for domino in dominoes:
        if tuple(sorted(domino)) in mpp:
            count += mpp.get(tuple(sorted(domino)))
            mpp[tuple(sorted(domino))] += 1
        else:
            mpp[tuple(sorted(domino))] = 1
    return count             
print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))


def numEquivDominoPairs2(dominoes: list[list[int]]) -> int:
    num = [0] * 100
    count = 0
    for x,y in dominoes:
        val = x * 10 + y if x <= y else y * 10 + x
        count += num[val]
        num[val] += 1
    return count
print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))