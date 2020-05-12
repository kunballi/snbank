import random
import json
from datetime import datetime
from os import remove


time=datetime.now(tz=None)


#loggin out function
def logout():
    session_log=open('session.txt','a')
    #session_log.write(f'{time}:@ {details[0]}logged out\n')
    session_log.close()
    remove('session.txt')
    homepage()



# getting staff details to login
def get_details():
    user_name = input('Enter your username: ')
    user_password = input('Enter your password: ')
    details = [user_name, user_password]

    return details


# checking accout details
def check_acct():
    check_acct_number=input('Enter Account Number: ')
    customer_file=open('customer.txt','r').read()
    customer_details_list=customer_file.splitlines()
    count=1
    found=False
    for item in customer_details_list:
        details=json.loads(item)
        if check_acct_number==details['Account Number']:
            print(details)
            found=True
        if count==len(customer_details_list) and not found:
            print('Account does not exist')
        count+=1
    action()




# getting details for account opening
def create_acct():
    acct_name = input('Enter Name: ')
    while True:
        opening_bal = input('Enter opening balance: ')

        try:
            balance = int(opening_bal)
            break
        except ValueError:
            print('invalid input,Enter a numeric value')
    acct_type = input('Enter account type: ')
    acct_email = input('Enter account Email: ')
    random_acct = ''.join(str(random.randint(0, 9)) for i in range(10))
    acct_details = [acct_name, opening_bal, acct_type, acct_email, random_acct]
    print('Name:', acct_details[0], 'Opening Balance:', acct_details[1], 'Account Type:',
          acct_details[2], 'Account Email:', acct_details[3], 'Account Number:', acct_details[4])
    customer_details = {'Account Name': acct_name, 'Opening Balance': opening_bal,
                        'Account Type': acct_type, 'Account Email': acct_email, 'Account Number': random_acct}
    customer_file = open('customer.txt', 'a')
    customer_file.write(json.dumps(customer_details))
    customer_file.write('\n')
    customer_file.close()
    action()

def action():
    login_success = int(input('LOGIN SUCCESSFUL,Enter 1 to Create New Bank Account,2 to Check Account Details,3 to Log Out: '))
    if login_success == 1:
        create_acct()
    elif login_success==2:
        check_acct()
    elif login_success==3:
        logout()
    else:
        print('invalid input')
        action()



def login():


    new_staff_list = []
    details = get_details()
    staff_details = open('staff.txt')
    staff_list = staff_details.read()
    staff_lists = staff_list.splitlines()
    for staff in staff_lists:
        new_staff_list.append(staff.split())
        # print(new_staff_list)
    count = 1
    logged = False
    for item in new_staff_list:
        if details[0] == item[0] and details[1] == item[1]:
            logged = True
            session_logged=open('session.txt','w+')
            #session_logged.write(f'{time}:@{details[0]} logged in\n')
            session_logged.close()
            action()
        if count==len(new_staff_list) and not logged :
            print('invalid username or password')
        count+=1
    login()

#homepage login
def homepage():

    staff_login = input('Enter login if you would like to login or No if you want to close the app: ').upper()
    if staff_login == 'LOGIN':
        login()
    elif staff_login=='NO':
        exit(0)
    else:
        print('invalid input')
        homepage()


#main project
homepage()
