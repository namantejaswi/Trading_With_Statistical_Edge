
from math import log, sqrt
import random
from typing import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as stat


print("We will assert that the pseudo random number we gnerate is statistically reliable, i,e consistent with law of large numbers")

roullete_log={}
frequency_log=[0]*37 # 37 pockets indexed from 0 t 36

Montecarlo_Sim_Instances=1000000 # 1 Million Spins of the wheel

for x in range(Montecarlo_Sim_Instances):
    roullete_log[x]=random.randint(0,36)    #randint is inclusive of both start and end
    
    
for z in range(Montecarlo_Sim_Instances):
    for k in range(0,37):               #can use a hash map to reduce from O(n^2)
        if(roullete_log[z]==k):
            frequency_log[k]=frequency_log[k]+1
            
print("We have stored the number of times we got each number on the roullete for ")


for i in range (0,37,1):
    print(" The % times we got ",i,' was ',frequency_log[i]*100/1000000, '\n')

Expected_frequency=(1/37)*100
print("Theoretically we expect to get a particular ",Expected_frequency, "% times" )

Mean_Expected_value= (Expected_frequency/100)*1000000 
print('Absolute Expected freuqncy of after 1 million spins for each number is ',Mean_Expected_value )

#plt.plot(np.linspace(0, 36, num=37),frequency_log,marker="o",mfc='r',mec='r')

plt.bar(np.linspace(0, 36, num=37),frequency_log)

title_font = {'family': 'serif', 'color': 'darkred', 'size': 18}
plt.title("Roullete Spin outcomes",fontdict=title_font)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()

#Standard_Deviation = stat.stdev(frequency_log)
#normalised_sd = Standard_Deviation/Mean_Expected_value

#print("Normalised Standard deviation ", normalised_sd*100,'%')

Bank_Balance_log = []
Bank_Balance = int(0)
Bank_Balance = int(input("How much money do you have? "))


def roullete_spin():
    r = random.randint(0, 36)
    print("The wheel shows up the number ", r)
    return r

def lost(wager):
    global Bank_Balance
    print("Sorry you lost ", wager, "$ this time")
    Bank_Balance = Bank_Balance-wager
    print("You have", Bank_Balance, "$ left")
    Bank_Balance_log.append(int(Bank_Balance))


def won_redblack(wager):
    global Bank_Balance
    print("Lets goooo you have won ", wager*2, "$")
    Bank_Balance = Bank_Balance+(wager*2)
    print("You have", Bank_Balance, "$ left")
    Bank_Balance_log.append(int(Bank_Balance))

def won_green(wager):
    global Bank_Balance
    print("Lets goooo you have won ", wager*35, "$")
    Bank_Balance = Bank_Balance+(wager*35)
    print("You have", Bank_Balance, "$ left")
    Bank_Balance_log.append(int(Bank_Balance))
    

continue_playing=0
print("Welcome to the casion Do you wish to play 1/0")
continue_playing=int(input())
Bank_Balance_log.append(int(Bank_Balance))

while(int(continue_playing)==1):
    continue_betting=0
    print("DO you want to continue betting 1 for Yes 0 to go home")
    continue_betting=int(input())
    if(continue_betting==0):
        print("Sad to see you go")
        print("You have ",Bank_Balance," $ Left in your bank account")
        Bank_Balance_log.append(int(Bank_Balance))
        break
    elif(continue_betting==1):
        bet_choice=int(0)
        wager=int(0)
        bet_number=int(0)
        Even_odd=int(0)
        Red_Black=int(0)
    
        print("Gambling Odds and Payout \n Even Number/Red-Black odds 18;37, payout 1:2 Odd Number 18:37 1:2, \n Specific NUmber prob 1:37 payout 1:35  ")
        print("Enter your bet type 1,2,3")
        bet_choice=int(input())
        print("Enter the bet amount ")
        wager=int(input())
        if(wager>Bank_Balance):
            print('Time to call the bouncers')
            break #your bones xD

        if(bet_choice==1 or bet_choice==2):
            print("Do you wish to bet on Red or Black, Even or Odd 0 or 1")
            Even_odd=int(input())
            
            rs=random.randint(0,36)
            if(rs==0):
                lost(wager)

            elif(rs%2==1):
                if(Even_odd==1):
                    won_redblack(wager)

                elif(Even_odd==0):
                    lost(wager)
                
            elif(rs%2==0):
                if(Even_odd==0):
                    won_redblack(wager)

                elif(Even_odd==1):
                    lost(wager)

        if(bet_choice==3):
            print("Enter the number on which you want to bet in from 0 to 36")
            bet_number = int(input())            
            rs=random.randint(0,36)
            
            if(rs==bet_number):
                won_green(wager)
                
            elif(rs!=bet_number):
                lost(wager)
                
plt.plot(Bank_Balance_log)    
plt.title("Balance Log")

plt.show()

  
def martingle_sim():

    m = int(input("Enter your bet balance "))
    ib = int(input("Enter your first bet amount"))
    martingle_log=[]
    martingle_log.append(m)
    
    we_always_bet=0 #Even
    current_wager=ib;
    coin_log=[]
    
    while(m>0):
        
        res=random.randint(0,36)     
        if(res==0):
            m=m-current_wager
            current_wager=2*current_wager;
            martingle_log.append(m)
            coin_log.append("!")
            
            
        elif(res%2==1):
            m = m-current_wager
            current_wager = 2*current_wager
            coin_log.append("Odd")
            martingle_log.append(m)
            
        elif(res%2==0):
            m = m+current_wager
            current_wager = current_wager/2
            martingle_log.append(m)
            coin_log.append("Odd")
            
    plt.plot(martingle_log,color='r',linewidth=2,marker=".",mfc='b')
    plt.xlabel("Number of bets")
    plt.ylabel("Bank Balance")
    plt.title("Martingle Simulation")
    plt.show()
    
martingle_sim()


def max_consecutive_defeat():

    balance = float(input("Enter your bet balance "))
    loss_count = int(0)
    initial_bet_size = float(input("Enter your first bet amount"))
    b_log=[]
    b_log.append(balance)
    while(balance > 0):

        balance = balance-((2**(loss_count))*initial_bet_size)
        loss_count = loss_count+1
        print(balance, loss_count)
        b_log.append(balance)
    # wont have capital for last bet though
    print("You will be bankrupted at ", loss_count, " straight losses in a row")

    plt.plot(b_log)
    plt.xlabel("Successive losses")
    plt.ylabel("Balance")
    plt.title("Number of straight losses to bankrupt")
    plt.show()

max_consecutive_defeat()

def max_consecutive_binaryoutcome():
    mch = 0             #max_consecutive_head
    mct = 0             #max_consecutive_tails
    streak_h = 0
    streak_t = 0
    output = []
    for x in range(10000000):
        r = random.randint(0, 1)
        if(r == 0):
            output.append(int(0))
            streak_t = 0
            if(output[x-1] == 0 and x != 0):
                streak_h = streak_h+1
                if(streak_h > mch):
                    mch = streak_h
        if(r == 1):
            output.append(int(1))
            streak_h = 0
            if(output[x-1] == 1 and x != 0):
                streak_t = streak_t+1
                if(streak_t > mct):
                    mct = streak_t

    print("In 10 million flips/simulation we get a maximumum of ",
        mch, " 0`s or blacks or heads or evens in a row which has a probability of ",(0.5)**mch)
    
    print("an we get a maximumum of ", mct,
          " 1`s or reds or tails or odds in a row which has a probability of ", (0.5)**mct)

    print("Thus the martingle is bound to fail if we play long enough as a series of losing outcomes dradowns us exponentially")

    
max_consecutive_binaryoutcome()


# What amount we bet is determined by The Kelly Critrion

def expected_value():
    
    bet_amount = float(input("Enter the bet amount"))
    prob_w = float(input("Enter the probability of winning"))
    payout_w = float(input("Enter the payout per unit upon winning"))
    payin_l = float(input("Enter the payin per unit upon losing"))

    eval_1 = float((prob_w*payout_w+((1-prob_w)*(-payin_l)))*bet_amount)

    print("The expected value for a single play is ",
          eval_1, " and after 1000 plays ", eval_1*1000)
    if(eval_1 < 0):
        print("One is destined to lose if he plays the game")
        print("The casino expects to make", eval_1,
              " on each bet you make and after 1000 plays ", eval_1*1000)
        print("  Thus we trade/bet when we have a positive expected value ")
    if(eval_1 > 0):
        print("This is a favourable bet with an expected value of ",
              eval_1, " for one play and after 1000 plays ", eval_1*1000)

    return [eval_1, prob_w, payout_w, payin_l]

# What amount we bet is determined by The Kelly Critrion


def kelly_bet_size(p_w, po_w, pi_l):

    #k               #Kelly % to bet
    #p               #Probability of win
    #q=1-p           #Probability of loss
    #r               #Reward:Risk, payout odds
    # k=p-(q/r)

    ev=p_w*po_w+((1-p_w)*(-pi_l))
    
    rr = float(po_w/pi_l)
    
    k = float((p_w-((1-p_w)/rr))*100)
    if(ev > 0):        
        print("One should bet ", k, "% of the available balance")
    elif(ev<=0):
        print("One should not bet")

    return k

eva, p_w, po_w, pi_l = expected_value()
kelly_bet_size(p_w, po_w, pi_l)


def table_limit():

#Consider the red black and even odd betting,number betting from casino's perspective

#E(x)=P(w)*win_val+(1-p(W)*lose_val)

#expected_value=19/37*(1)+18/37*(-1)=0.0270
#expected_value=36/37(1)+1/37*(-35)=0.0270

    kelly_casino=kelly_bet_size(19/37,1,1)
    
    print("Ideally a casino would have a table limit of a maximum of ",kelly_casino,"% of its funds at any point of time")
    print("As we saw with a fair martingle that a run of losses may bankrupt us even though the expected value is 0")
  
    print("Thus we must bet  kelly% of our funds also not on every loss the bet size would reduce and on every win it would increase contrary to our martingle aaproach")    
table_limit()

def kelly_sim():
    

    casino_log=[]
    #We replicate a scenario  as if we are the casino
    
    k_casino = kelly_bet_size(19/37, 1, 1)
    
    initial_casino_balance=1000
    casino_balance=initial_casino_balance
    casino_log.append(initial_casino_balance)
    
    initial_casino_bet=(k_casino/100)*initial_casino_balance
    
    #we(casino) always bet even and zero 
    
    bet=initial_casino_bet
    for x in range(1000000):
        spin=int(random.randint(0,36))
        if(spin%2==0):
            casino_balance=casino_balance+bet
            casino_log.append(casino_balance)
            bet=(k_casino/100)*casino_balance
        elif(spin%2==1):
            casino_balance=casino_balance-bet
            casino_log.append(casino_balance)
            bet=(k_casino/100)*casino_balance   
    
    print(casino_balance)
    plt.plot(casino_log)
    plt.yscale('log',base=10)

    plt.xlabel("Number of plays")
    plt.ylabel("Casino bank balance")
    plt.title("Casino allowing bets using kelly criteria a Million plays")
    plt.show()
kelly_sim()




        
