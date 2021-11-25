import numpy as np
import pymysql
from . import my_sql_conn
from xor_project import products, cart, order
import os


class Customer:

    global user, c_usr

    def create(self):

        #sql_q = "insert into customer values()"
        card_det = 0

        name = input('Enter your name:')
        idd = int(input('Enter ID:'))
        address = input('Enter your address:')
        mobile = int(input('Enter your mobile:'))
        email = input('Enter your email:')
        password = input('Enter new password (5 character only):')
        pref_payment = input('cash or card:')
        print()
        if pref_payment == 'card':
            card_det = int(input('Enter your card number:'))


        sql_q = "insert into customer(id,name,address,email,mobile,password,pay_op, card) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        que = (idd, name, address, email, mobile, password, pref_payment, card_det)

        cur, conn = my_sql_conn.connect_to_db()

        try:
            cur.execute(sql_q, que)

            conn.commit()

        except Exception as e:

            print(e)
            conn.rollback()

        print(cur.rowcount, "record inserted!")
        print('Your new account is create successfully!')
        print()

    def authenticate(self):

        db_name = None
        db_pass = None

        cur, conn = my_sql_conn.connect_to_db()

        user = input('Enter your name: ')
        psss = input('Enper your password:')

        sql = ' select * from customer'

        cur.execute(sql)

        result = cur.fetchall()

        for r in result:

            db_name = r[1]
            db_pass = r[5]

        if user == db_name and psss == db_pass:
            print('logging you in!')
            print()

            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

            clearConsole()
            self.cus_home(user)

        else:
            print('Invalid login credentials!...Please try again')
            self.authenticate()

    def cus_home(self, c_usr):
        
        global by_add
        # cus home page and to add products to cart
        print()
        print('Welcome to shop!', c_usr)
        print()
        print("1. Type 'buy' to buy a product")
        print("2. Type 'view' to view products")
        print("3. Type 'remove' to remove product from cart")
        print("4. Type 'view_or' to view your orders")
        print("5. Type 'cart' to update your cart details")
        print("6. Type 'update' to update your order details")
        #print('What would like to do, view product,buy product,remove product from cart, view orders:')
        print()

        opt = input('Enter your option(buy or view or remove):')
        print()

        if opt == 'view':

            pp = products.Products()
            #pp.view_product(c_usr)
            pp.v_p(c_usr)

        elif opt == 'buy':
            pp = products.Products()
            cc = cart.Cart()
            pp.view_product(c_usr)
            print()
            by_add = input('Enter the product name, your id and quantity of the product that you like to add to your cart:').split(',')
            cc.add_product(by_add[0], by_add[2], by_add[1])
            fi = open('demo.txt', 'w')
            fi.write(by_add[0])
            fi.close()
            print()
            print('Taking you to your cart')
            cc.view_cart(by_add[0], c_usr)

        elif opt == 'remove':
            ca = cart.Cart()
            ca.remove_product(c_usr)

        elif opt == 'view_or':
            orr = order.Order()
            orr.tak_or(c_usr)

        elif opt == 'update':
            ork = order.Order()
            ork.update_order(c_usr)
            
        elif opt == 'cart':
            fi = open('demo.txt', 'r')
            pp = fi.read()
            #fi.close()
            cc2 = cart.Cart()
            cc2.view_cart(pp, c_usr)

        else:
            print('Invalid input!...try again!')
            self.cus_home(c_usr)

    def buy(self):
        print('Enter the name of the product you want to b')





