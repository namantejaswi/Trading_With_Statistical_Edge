
import random
import matplotlib.pyplot as plt

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
  
    print("Thus we must bet  kelly% of our funds also1 on every loss the bet size would reduce and on every win it would increase contrary to our martingle aaproach")    
table_limit()

def kelly_sim():
    

    casino_log=[]
    #We replicate a scenario  as if we are the casino
    
    k_casino = kelly_bet_size(18/37, 1, 1)
    
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
            if(casino_balance<0):
                print("Interesting we should not have been here")
                break
        elif(spin%2==1):
            casino_balance=casino_balance-bet
            casino_log.append(casino_balance)
            bet=(k_casino/100)*casino_balance   
            if(casino_balance<0):
                print("Interesting we should not have been here")
                break
            
    
    print(casino_balance)
    plt.plot(casino_log)
    plt.yscale('log',base=10)

    plt.xlabel("Number of plays")
    plt.ylabel("Casino bank balance")
    plt.title("Casino allowing bets using kelly criteria a Million plays")
    plt.show()
kelly_sim()

