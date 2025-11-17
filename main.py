# Game of Stone,Paper and scissor
import random 
'''
-1 for stone
0 for paper
1 for scissor
'''
computer=random.choice([-1,0,1])
user_input=input('enter the choice:')
user_dict={'stone':-1,'paper':0,'scissor':1}
reverse_dict={-1:'stone',0:'paper',1:'scissor'}
you = user_dict[user_input]
# now we have two numbers ,computer and user
print(f'You choose {reverse_dict[you]}\nComputer choose {reverse_dict[computer]}')
if computer==you:
    print('Its a draw')
else:
    if(computer==-1 and you==0):
        print('You Win!')
    elif(computer==-1 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print('You Lose!')
    elif(computer==0 and you==1):
        print('You Win!')
    elif(computer==1 and you==-1):
        print('You Win!')
    elif(computer==1 and you==0):
        print("You Lose!")
    else:
        print('Something went wrong')