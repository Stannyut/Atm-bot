
# An ATM bot
balance = 5000
pin = 1234
print('Welcome to Stann Bank')
enter = int(input('Enter 1 to continue  2 to costomer care services or 3 to cancel '))
if enter == 1:
    for i in range(3):
        pin = int(input('Enter your password: '))
    if pin == 1234:
        print('Welcome to your Stann account!')
        print("Type 'dep' to deposit, 'wtdrw' to withdraw, 'bal' to check balance, or 'pin'to change pin")
        procedure = input('Type any of the above options: ').lower()
        if procedure == 'dep':
            dep = int(input('Enter the amount you wish to deposit: '))
            balance += dep
        elif procedure == 'wtdrw':
            wtdrw = int(input('Enter the amount you wish to withdraw: '))
            balance -= wtdrw    
            print('Withdrawal of ksh',wtdrw, ' successful')
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
elif enter == 2:
    print('welcome to costomer care services!')
    service = input('press 1 to talk to an agent, 2 to get a bank statement')
    if service == 1:
        print('Kindly hold as we connect you to the next available agent!')
    elif service == 2:
        print('This is your bank statement', balance )
    else:
        print('You pressed the wrong button! Try again!')
elif enter == 3:
    print('Happy banking with Stann bank!') 


    # pin = int(input('Enter your password: '))   
    
                

