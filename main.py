
# An ATM bot
balance = 5000
pin = 1234
print('Welcome to Stann Bank')
enter = int(input('Enter 1 to continue or 2 to cancel '))
while enter == 1:
    pin = int(input('Enter your password: '))
    if pin == 1234:
        print('Welcome to your Stann account!')
        print("Type 'dep' to deposit,or 'bal' to check balance or 'pin'to change pin")
        procedure = input('Type any of the above options: ').lower()
        if procedure == 'dep':
            dep = int(input('Enter the amount you wish to deposit: '))
            balance += dep
            print('Deposit of ksh',dep, ' successful')
            print('Total account balance is ksh',balance)
        elif procedure == 'bal':
            print('Account balance is ksh', balance) 
        elif procedure == 'pin':
            #pin = int(input('Enter the new passcode: '))
            #print('Pin change successful!')
            print('Service currently unavailable!')
        elif procedure != 'dep' or procedure != 'bal' or procedure != 'pin': 
            print('Incorrect format or spelling, try again!')
            procedure = input('Type any of the above options: ').lower()
    else:
        print('Wrong password, Try again!')
    # pin = int(input('Enter your password: '))   
print('Happy banking with Stann bank!')     
                

