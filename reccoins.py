
def recDC(coinValueList, change, knownRseults):
    minCoins = change
    if change in coinValueList:
        knownRseults[change] = 1
        return 1
    elif knownRseults[change] > 0:
        return knownRseults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownRseults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownRseults[change] = minCoins
    return minCoins
print(recDC([1, 5, 10, 21, 25], 63, [0]*64))