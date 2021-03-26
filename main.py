import random
option = ['rock', 'paper', 'sci']

n=0
m=0
print ("Welcome to Rock-Paper-Scissors!")

while n<=3 or m<=3:

    userchoice = input("Please enter your choice... rock, paper, sci:")
    compchoice = random.choice(option)


    if userchoice == 'rock' and compchoice == 'sci':
       print ('You get a point!')
       n +=1
       print ("Your points are",n)

    if userchoice == 'paper' and compchoice == 'rock':
        print ("You get a point!")
        n +=1
        print ("Your points are",n)

    
    if userchoice == 'sci' and compchoice == 'paper':
        print ("You get a point!")
        n +=1
        print ("Your points are",n)

    
    if userchoice == 'rock' and compchoice == 'paper':
        print ("Opponent gained a point!")
        m +=1
        print ("Opponents points are",n)


    if userchoice == 'sci' and compchoice == 'rock':
        print ("Opponent gained a point!")
        m +=1
        print ("Opponents points are",n)


    if userchoice == 'paper' and compchoice == 'sci':
        print ("Opponent gained a point!")
        m +=1
        print ("Opponents points are",n)


    if userchoice == compchoice:
        print ("Draw!")

    
    else:
        if n ==3:
           print ("You Win!")
        if m ==3:
            print ("You Lose! :(")
            break


##E U R E K A ! ! It Works!