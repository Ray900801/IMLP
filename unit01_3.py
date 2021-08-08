import random as rd
MIN=0
MAX=100
ans=rd.randint(1,99)
count=1
while True:
    guess=int(input("input a interger in (%d,%d)"%(MIN,MAX)))
    if guess<MAX and guess>MIN:
        if guess==ans:
            print("you got it")
            break
        elif guess<ans:
            print("smaller than the answer and you have done %d guess"%(count))
            MIN=guess
            count+=1
        else:
            print("greater than the answer and you have done %d gusee"%(count))
            MAX=guess
            count+=1
    else:
        print("could you do anything right?!")       
    

