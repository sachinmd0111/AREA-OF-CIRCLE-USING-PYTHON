# -*- coding: utf-8 -*- p

'''a=0
s=0
b=['0','1','2','3','4','5','6','7','8','9','10']
player1=int(input("Enter a number between 1 and 10:"))
player2=int(input("Enter a number between 1 and 10 :"))
if player1 and player2 in b:
 if player1 != player2 :
       s=player1
       a+=s  
  continue
 else :
       a=player1
       print("YOU ARE OUT")
       print("YOUR SCORE IS ",a)
       break
else:
     print("INVALID INPUT")
'''
'''
count=0
score=0
inp=input("HI, READY FOR QUIZ: (YES OR NO)  ").casefold()
if inp=='yes': 
 print("YOUR FIRST QUESTION IS \n")
 print("WHO IS THE CEO OF MICROSOFT \n") 
 print("YOUR OPTIONS ARE\n A.SATYA NADELLA\n B.SUNDAR PICHAI\n C.ELON MUSK\n D.STEVE JOBS\n")
 choice=input("Enter your option\n ").casefold()
 if choice=='a':
     score+=1           
 else:
     score=score
 count+=1
        
 print("\nYOUR SECOND QUESTION IS \n")
 print("WHO IS THE CEO OF GOOGLE \n")
 print("YOUR OPTIONS ARE\n A.SATYA NADELLA\n B.SUNDAR PICHAI\n C.ELON MUSK\n D.STEVE JOBS\n")
 choice=input("Enter your option\n ").casefold()
 if choice=='b':
    score+=1
 else:
    score=score
 count+=1
 print("\nYOUR THIRD QUESTION IS\n ")
 print("WHO IS CEO OF APPLE")
 print("YOUR OPTIONS ARE\n A.SATYA NADELLA\n B.SUNDAR PICHAI\n C.ELON MUSK\n D.STEVE JOBS\n")
 choice=input("Enter your option \n").casefold()
 if choice=='d':
    score+=1
 else:
    score=score
 count+=1
 print("YOUR FINAL SCORE IS ",score,"on",count) 
 print("CONGRATULATIONS!!! ")            
else:
    print("THANK YOU")
'''
'''
a=['1','2','3','4','5','6','7','8','9','10']
b=['1','2','3','4','5','6','7','8','9','10']
runs=0
player1=int(input("Enter a number between 0 and 11 "))
player2=int(input("Enter a numberbetween 0 and 11 "))
for player1 in a:
    for player2 in b:
        if player1 != player2:
            score=int(player1)
        
            runs+=score
            
  #      else:
 #           print("OUT !!")
#print("TOTAL RUNS IS ",runs)
'''
import math
fname=float(input("Input the radius of the circle "))
area= math.pi*fname**2
print("The area of the circle with radius",fname,"is ",area)
            
            
            
            
        




