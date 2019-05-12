# DC Project
# 4B/5B Block Coding Technique

import random

validCodewords = {'0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101',
                  '0100': '01010', '0101': '01011', '0110': '01110', '0111': '01111',
                  '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
                  '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101'}

print("Input 4 bit Dataword in binary :")
dataWord = input()

codeWord = validCodewords[dataWord]
print("corresponding codeword : ", codeWord)

errorPerc = random.randrange(100)
print(errorPerc)

if errorPerc > 7:
    errorCodeWord = bin(random.randrange(31)).replace("0b", "")
    errorCodeWord = errorCodeWord.zfill(5)
    print("errorCodeword = ", errorCodeWord)

    if errorCodeWord in validCodewords.values():
        if errorCodeWord == codeWord:
            print("LUCKY")
        else:
            print("Error Undetected")
    else:
        print("Error... Discarding Packet !...")
else:
    print("PROPER TRANSMISSION")