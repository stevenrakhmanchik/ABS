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
ver = 'ABS Brute-Force Attack Penetration Testing' #version number
#Advanced Binary Scrambler Encryption Algorithm Brute Force Penetration Testing
from datetime import datetime
import numpy as np
import hmac
import hashlib
import base64
from string import printable
from itertools import product

startTime = datetime.now()

print("ABS " + ver + "\nAdvanced Binary Scrambler\n-----------------------")
brute_force = open('Brute_Force.txt', 'w+')
def Penetration_Testing():
    string = input("Enter Encrypted String To Brute Force: ")
    for length in range(1, 12):
        print(str(length) + '/12')
        password_to_attempt = product(printable, repeat=length)
        for attempt in password_to_attempt:
            attempt = ''.join(attempt)
            brute_force.write(attempt + ' ')
            str1 = ASA(attempt, 'd', string)
            brute_force.write(str1 + '\n')
            
def ASA(key, op, raw):            
    def hasher(key):
        key = bytes(key, 'utf-8')
        secret = bytes('Advanced Binary Scrambler', 'utf-8')
        message = base64.b64encode(hmac.new(key, secret, digestmod=hashlib.sha512).digest())
        message = bytes(str(message), 'utf-8')
        key = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha512).digest())
        return(key)
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
    key = hasher(key)
    key = str(key)
    key2 = ''
    for x in range(0, len(key)):
        key2 = key2 + str(ord(str(key[x])))

    def ASA_ENC_DEC(key):
        if op == 'd':
            key = key[::-1]
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
        return(str1)
            
    if op.lower() == 'e' or op.lower() == 'encrypt':
        str1 = ASA_ENC_DEC(key2)
    if op.lower() == 'd' or op.lower() == 'decrypt':
        str1 = ASA_ENC_DEC(key2)
    return(str1)
Penetration_Testing()
time_spent = str(datetime.now() - startTime)
brute_force.write(time_spent)
brute_force.close()
