# ________  ________  ________    _______      ________     
#|\   __  \|\   __  \|\   ____\  /  ___  \    |\   __  \    
#\ \  \|\  \ \  \|\ /\ \  \___|_/__/|_/  /|   \ \  \|\  \   
# \ \   __  \ \   __  \ \_____  \__|//  / /    \ \  \\\  \  
#  \ \  \ \  \ \  \|\  \|____|\  \  /  /_/__  __\ \  \\\  \ 
#   \ \__\ \__\ \_______\____\_\  \|\________\\__\ \_______\
#    \|__|\|__|\|_______|\_________\\|_______\|__|\|_______|
#                       \|_________|                                                                                                                                                       
#Steven Rakhmanchik (C) 2019
#-------------------------------------------------------------------#
ver = 'Stable Release 2.5 Revision' #version number
#Advanced Binary Scrambler Encryption Algorithm
import numpy as np
import hmac
import hashlib
import base64
print("ABS " + ver + "\nAdvanced Binary Scrambler\n-----------------------")
def hasher(key):
    key = bytes(key, 'utf-8')
    secret = bytes('Advanced Binary Scrambler', 'utf-8')
    message = base64.b64encode(hmac.new(key, secret, digestmod=hashlib.sha512).digest())
    message = bytes(str(message), 'utf-8')
    key = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha512).digest())
    return(key)
raw = input("Enter String: ")
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
op = input("Operation (e/d): ")
key = input("Enter Key: ")
key = hasher(key)
key = str(key)
key2 = ''
for x in range(0, len(key)):
    key2 = key2 + str(ord(str(key[x])))

def ASA_ENC_DEC(key):
    if op == 'd':
        key = key[::-1]
    for t in range(0,20):
        for x in key:
            q = int(x) % c
            w = int(x) % d
            if op == 'e':
                a = mtx[w].tolist()
                a.reverse()
                mtx[w] = a
                a = mtx[:, q].tolist()
                a.reverse()
                mtx[: ,q] = a
            if op == 'd':
                a = mtx[:, q].tolist()
                a.reverse()
                mtx[: ,q] = a
                a = mtx[w].tolist()
                a.reverse()
                mtx[w] = a
    mtx1 = mtx.tolist()
    str1 = ''
    for x in mtx1:
        for y in x:
            str1 = str1 + str(y)
    print(str1)
        
if op.lower() == 'e' or op.lower() == 'encrypt':
    ASA_ENC_DEC(key2)
if op.lower() == 'd' or op.lower() == 'decrypt':
    ASA_ENC_DEC(key2)
#Steven Rakhmanchik (C) 2019
