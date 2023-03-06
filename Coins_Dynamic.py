from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):

    if amount == 0: # The base case
        return 0
    else:           # The recursive case
    
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins # If we can give change
            if (amount - currentCoin) >= 0:
            
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                
        # Keep the best
        minCoins = min(minCoins, currentMin) 
        return minCoins
    
# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):

    # Create the initial tables
    size = len(coins)
    dp_table = []
    for i in range(size):
        dp_table.append([0]*(amount+1))
    
    # Fill in the base case(s)
    # Fill in the rest of the table
    for i in range(size):
        for j in range(amount+1):
            if j == 0:
                dp_table[i][j] = 0
            elif i == 0:
                dp_table[i][j] = 1+ dp_table[i][j-coins[i]] 
            elif coins[i] > j:
                dp_table[i][j] = dp_table[i-1][j]
            else:
                dp_table[i][j] = min(1+dp_table[i][j-coins[i]],dp_table[i-1][j])

    
    # Perform the traceback to print result
    i = size - 1
    j = amount
    
    min_amount = amount
    
    min_coins = []
    while min_amount > 0:

        if i == 0:
            min_coins.append(coins[i])
            min_amount = min_amount - coins[i]
            j = min_amount-coins[i]
        else:
            current = dp_table[i][j]
            if current != dp_table[i - 1][j]:
                min_coins.append(coins[i])
                j = min_amount-coins[i]
                min_amount = min_amount - coins[i]
            
            else:
                i -= 1
                
    # print the coins array
    print("Min coin values:",min_coins)
    
    return dp_table[size - 1][amount] # return optimal number of coins

C = [1, 5, 10, 12, 25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: ')) 
assert A >= 0
print("DAC:") 
t1 = time()
numCoins = DACcoins(C,A) 
t2 = time()
print("optimal:",numCoins," in time: ",round((t2 - t1)*1000,1),"ms")

print() 
print("DP:") 
t1 = time()
numCoins = DPcoins(C,A) 
t2 = time()
print("optimal:",numCoins," in time: ",round((t2 - t1)*1000,1),"ms")
