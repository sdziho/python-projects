def vratiRijecnik(matrica):
    col = len(matrica)
    if(col < 1):
        print("Matrica je prazna")
        return
    row = len(matrica[0])
    for r in matrica:
        if len(r) != row:
            print("Matrica nije kvadratna")
            return
    for i in range(col):
        matrica[i] = convertBinaryArrayToInt(matrica[i])
    rjecnik = []
    for key in range(2 ** col):
        word = 0
        for currentKeyDigitIndex in range(col):
            keyDigit = key & (2 ** currentKeyDigitIndex)
            if(keyDigit != 0):
                word ^= matrica[currentKeyDigitIndex]
        rjecnik.append(word)
    return rjecnik

def convertBinaryArrayToInt(binary):
    result = 0
    length = len(binary)
    for i in range(length):
        result += binary[i] * 2 ** (length - 1 - i)
    return result
    
def printBinaryDictArray(dictArray):
    for i in range(len(dictArray)):
        strKey = "{0:04b}".format(i) [::-1]
        print("Kljuc: {0} Rijec: {1:07b}".format(strKey, dictArray[i]))


matrica = [
    [1,0,0,0,1,1,0], 
    [0,1,0,0,0,1,1],
    [0,0,1,0,1,1,1],
    [0,0,0,1,1,0,1]
]

rjecnik = vratiRijecnik(matrica)
print(rjecnik)
printBinaryDictArray(rjecnik)