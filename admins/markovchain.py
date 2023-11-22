import numpy as np
import random as rm
# The statespace 
states = ["Investment","Returnamount","Profit","Loss"]

# Possible sequences of states
transitionName = [["II","IR","IP","IL"],["RI","RR","RP","RL",],["PI","PR","PP","PL",],["LI","LR","LP","LL",]]

# Probabilities matrix (transition matrix)
transitionMatrix =[[330000,479166,70000,55000],[550000,85000,101666,120833],[160000,297500,1325000,41667],[319273,350833,22500,198968]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 4:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay, you should move on!! ;)")
#All is gonna be okay, you should move on!! ;)


# A function that implements the Markov model to business opportunity
def opportunity_process(business):
    # Choose the starting state
    opportunityToday='Investment'
    print("Start state: " + opportunityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    opportunityList = [opportunityToday]
    i = 0
    # To calculate the probability of the opportunityList
    prob = 1
    while i != business:
        if opportunityToday == "Investment":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "II":
                prob = prob * 330000
                opportunityList.append("Investment")
                pass
            elif change == "IR":
                prob = prob * 479166
                opportunityToday = "Returnamount"
                opportunityList.append("Returnamount")
            elif change == "IP":
                prob = prob * 70000
                opportunityToday = "Profit"
                opportunityList.append("Profit")
            else:
                prob = prob * 55000
                opportunityToday = "Loss"
                opportunityList.append("Loss")
        elif opportunityToday == "Returnamount":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 85000
                opportunityList.append("Returnamount")
                pass
            elif change == "RI":
                prob = prob * 550000
                opportunityToday = "Investment"
                opportunityList.append("Investment")
            elif change == "RP":
                prob = prob *101666
                opportunityToday = "Profit"
                opportunityList.append("Profit")
            else:
                prob = prob *120833
                opportunityToday = "Loss"
                opportunityList.append("Loss")
        elif opportunityToday == "Profit":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "PP":
                prob = prob * 13250000
                opportunityList.append("Profit")
                pass
            elif change == "PI":
                prob = prob * 160000
                opportunityToday = "Investment"
                opportunityList.append("Investment")
            elif change == "PR":
                prob = prob * 297500
                opportunityToday = "Returnamount"
                opportunityList.append("Returnamount")
            else:
                prob = prob * 41667
                opportunityToday = "Loss"
                opportunityList.append("Loss")
        elif opportunityToday == "Loss":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "LL":
                prob = prob * 198968
                opportunityList.append("Loss")
                pass
            elif change == "LI":
                prob = prob * 319273
                opportunityToday = "Investment"
                opportunityList.append("Investment")
            elif change == "PR":
                prob = prob * 350833
                opportunityToday = "Returnamount"
                opportunityList.append("Returnamount")
            else:
                prob = prob * 22500
                opportunityToday = "Profit"
                opportunityList.append("Profit")
        i += 1
    print("Possible states: " + str(opportunityList))
    print("End state after " + str(business) + " days: " + opportunityToday)
    print("Probability of the possible sequence of states: " + str(prob))

