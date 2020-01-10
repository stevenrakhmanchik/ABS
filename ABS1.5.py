# ________  ________  ________    _____      ________     
#|\   __  \|\   __  \|\   ____\  / __  \    |\   __  \    
#\ \  \|\  \ \  \|\ /\ \  \___|_|\/_|\  \   \ \  \|\  \   
# \ \   __  \ \   __  \ \_____  \|/ \ \  \   \ \  \\\  \  
#  \ \  \ \  \ \  \|\  \|____|\  \   \ \  \ __\ \  \\\  \ 
#   \ \__\ \__\ \_______\____\_\  \   \ \__\\__\ \_______\
#    \|__|\|__|\|_______|\_________\   \|__\|__|\|_______|
#                       \|_________|                                                                            
#Steven Rakhmanchik (C) 2019
#-------------------------------------------------------------------#
ver = 'Stable Release 1.0' #version number
#Advanced Binary Scrambler Encryption Algorithm
import numpy as np
import hashlib
print("ABS " + ver + "\nAdvanced Binary Scrambler\n-------------------------------------")
op = 'e'
def hasher(key):
    key = bytes(key, 'utf-8')
    key2 = hashlib.sha256(key)
    key = key2.digest()
    key = str(key, 'utf-8', 'ignore')
    return(key)

raw = input("Enter Binary String: ")
length = len(raw)
c = 1
d = length

for a in range(0, length):
    for b in range(0, length):
        if a * b == length and (a + b <= c + d):
            c = a
            d = b
list1 = [raw[start:start+c] for start in range(0, len(raw), c)]
list2 = []
for a in list1:
    a = list(a)
    list2.append(a)
mtx = np.array(list2)
op = 'e' 
op = input("Operation: ")
key = input("Enter Key: ")
key = hasher(key)
key = str(key)
key2 = ''
for x in range(0, len(key)):
    key2 = key2 + str(ord(str(key[x])))

def ABS_ENC_DEC(key):
    if op == 'd':
        key[::-1]
    print(key)
    for x in key:
        q = int(x) % c
        w = int(x) % d
        a = mtx[w].tolist()
        a.reverse()
        mtx[w] = a
        a = mtx[:, q].tolist()
        a.reverse()
        mtx[: ,q] = a
    mtx1 = mtx.tolist()
    str1 = ''
    for x in mtx1:
        for y in x:
            str1 = str1 + str(y)
    print(str1)
        
if op.lower() == 'e' or op.lower == 'encrypt':
    ABS_ENC_DEC(key2)
if op.lower() == 'd' or op.lower == 'decrypt':
    ABS_ENC_DEC(key2)
