from ctypes.wintypes import WORD
import random

word_bank=["tree","sky","man","pen","netflix","meeseeks"]
um=0
goodc=[]
badc=[]
word=random.choice(word_bank)

while um<6:

    for i in range(len(word)):
        if word[i] in goodc:
            print(word[i],end=" ")
        else:
            print("_ ",end =" ")

    if len(goodc)==len(word):
        y=input("write the word: ")
        ans=y.lower()
        if ans==word:
            print("you win")
            break

        
    else:
        karbar=input("please enter your guess: ")
        if len(karbar)!=1:
            print("mesle adam vared kon")

            
        Userchar=karbar.lower()
        
        if Userchar in word and len(karbar)==1:

            goodc.append(Userchar)
            print("✅")

        else:
            badc.append(Userchar)
            print("⛔")
            um +=1
    
if um<6:
    print("💕")   
else:
    print("game over")