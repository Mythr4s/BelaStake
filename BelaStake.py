"""""
Program: BelaStake.py
Author: ihashblox/Mythr4s
About: what this program does is calculate the staked amount of Bela over
a period of time.
"""""
# inputs
startBalance = float(input("Enter the investment amount: "))
rate = int(input("Enter the rate as a %: "))
time = int(input("Number of months you wish to stake: "))
# Convert the rate to a decimal number
rate = rate / 100
# Initialize the accumulator for the interest
totalInterest = 0.0
# Display the header for the table
print("%4s%18s%10s%16s" % \
("Starting balance","Interest", "Ending balance", "time",))

#computation
for time in range(1, time + 1):
    interest = startBalance * rate
endBalance = startBalance + interest
print("%4d%18.18f%10.18f%16.18f" % \
   (startBalance, interest,time, endBalance,))
startBalance = endBalance
totalInterest += interest

# Display the totals for the period
print("Ending balance: $%0.18f" % endBalance)
print("Total interest earned: $%0.18f" % totalInterest)
