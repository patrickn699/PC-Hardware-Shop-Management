#from xor_project import my_sql_conn
from xor_project import customer
from xor_project import admin

if __name__ == '__main__':
    print()
    print('--------------------------Welcome to mini PC hardware store!--------------------------')
    print('--------------------------Please login or create a new account.--------------------------')

    print()
    print("If you are a existing customer then type 'Y'")
    print("If you are a new customer then type 'N' for registration")
    print("If you are an admin then type 'A' to login")
    print()
    a = input('Hello!,Enter your choice Y/N/A:')

    if a == 'Y':
        cus1 = customer.Customer()
        cus1.authenticate()

    elif a == 'N':
        print('Please create a new account')
        cus = customer.Customer()
        cus.create()
        
    elif a == 'A':
        a1 = input('Are you the Admin? Y/N:')
        
        if a1 == 'Y':
            ad = admin.Admin()
            nm = ad.login()

            ad.admin_menu(nm)
        