# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console 
# input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = int(input("How much would you like to deposit? "))
        account = account + deposit
    elif action == "w":
        withdrow = int(input("How much would you like to withdrow? "))
        account = account - withdrow
    elif action == "b":
        print(account)
    else:
        quit()