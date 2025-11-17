#Guess the right number
import random
n = random.randint(1,100)
a=-1
gusses = 1
while(a!=n):
    a=int(input("Guess a number:"))
    if (a >n):
       print("Guess a smaller number")
       gusses+=1
    elif (a<n):
        print("Guess a greater number")
        gusses+=1
        
print(f'You Have Guessed the right number {n} in {gusses} attempts')
if gusses <= 5:
    print(' Excellent')
elif gusses > 5 and gusses <= 10:
    print('Very Good')
elif gusses >10 and gusses <= 15:
    print('Good')
else:
    print('Try taking lesser gusses next time')
