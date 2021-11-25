from xor_project import my_sql_conn
from xor_project import customer, cart
import datetime
import pandas as pd


class Order:

    global da

    def track_order(self, c_nm, pr_nm, p_mo, amtt, dt):

        cur, conn = my_sql_conn.connect_to_db()

        sql = "insert into orders(cuto_nm, pro_nm, payment_mode, amt, date) values (%s,%s,%s,%s,%s)"
        sql1 = "select * from orders"
        print(c_nm, pr_nm, p_mo, amtt, dt)

        va = (c_nm, pr_nm, p_mo, amtt, dt)

        try:
            cur.execute(sql,va)
            conn.commit()

        except Exception as e:
            print(e)
            conn.rollback()

        cur.execute(sql1)

        res = cur.fetchall()
        print('Your order details are:-')
        print()
        #print('Customer name', 'Product name', 'Payment method', 'Amount', 'Date')
        '''
        for i in res:
            print(i)
        '''
        df = pd.DataFrame(list(res), columns=['Id', 'Customer name', 'Product name', ' Payment method', 'Amount', 'Date'])
        print(df)
        print()

        k = input("Type 'b' to go to home page:")
        if k == 'b':
            c = customer.Customer()
            c.cus_home(c_nm)

    def tak_or(self, c_usr):

        # display the placed oreders and its total

        global pri, qn
        cur, conn = my_sql_conn.connect_to_db()

        sql = "Select * from orders"
        sqql = "select * from cart"
        cur.execute(sql)

        res = cur.fetchall()
        print('Your order details are:-')
        print()
        df = pd.DataFrame(list(res), columns=['Id', 'Customer name', 'Product name', ' Payment method', 'Amount', 'Date'])
        print(df)
        print()

        cur.execute(sql)

        result = cur.fetchall()

        try:
            '''
            for j in result:
                qn = j[4]
                pri += j[5]*qn
            print()
            print('Your order total is:', pri)
            print()
            '''
            pass

        except:
            print('You have no orders placed!')
            print()
        
        h = input("Type 'b' to go to home page:")
        if h == 'b':
            c = customer.Customer()
            c.cus_home(c_usr)

    def cancel(self, c_nm):

        #method to cancel the order

        cur, conn = my_sql_conn.connect_to_db()

        oc = input('Are you sure that you want to cancel your order?: Y/N')
        sql = "delete from orders where cuto_nm = '{}'".format(c_nm)

        if oc == 'Y' or oc == 'y':
            try:
                cur.execute(sql)
                conn.commit()
                cx = customer.Customer()
                cx.cus_home(c_nm)

            except Exception as e:
                print(e)
                conn.rollback()

        elif oc == 'N' or oc == 'n':
            cx = customer.Customer()
            cx.cus_home(c_nm)

    def payment(self, p_nm, cu_nm, amtt, c_usr):

        global c1

        cur, conn = my_sql_conn.connect_to_db()
        print('-----------------Welcome to NeoPass payment gateway-----------------')
        py = input("Enter your payment method cash or card:")
        print()

        if py == 'cash':
            da = datetime.datetime.now()
            da = da.strftime('%Y-%m-%d')
            print('order placed successfully:', da)
            print('your order will be delivered to your registered address')
            print('Please provide exact change to the delivery executive:')
            print('your estimated delivery will be in 5 days')
            print('Thanks for shopping!!')
            print()

            sqlp = "update products set quantity = quantity - 1 where name = '{}'".format(p_nm)

            try:
                cur.execute(sqlp)
                conn.commit()

                print()
                # print('Taking you to your home page:')
                print()
            except Exception as e:
                print(e)

            orr = input('Do you want to check your order? Y/N:')

            if orr == 'Y':
                self.track_order(pr_nm=p_nm, dt = da, c_nm=cu_nm,p_mo=py,amtt= amtt)

            else:
                ca = cart.Cart()
                ca.clear_cart(c_usr)
                c1 = customer.Customer()
                c1.cus_home(c_usr)

        elif py == 'card':

            # verify card no from customers table and the quantity should be reduced from products table
            ca = int(input('Please enter your card number:'))
            print('verifying the details please wait....')
            print()
            sql = "select * from customer"

            cur.execute(sql)
            result = cur.fetchall()

            for i in result:
                c1 = i[7]

            if ca == c1:

                # if card is valid place order
                da = datetime.datetime.now()
                da = da.strftime('%Y-%m-%d')
                print('order placed successfully:', da)
                print('your order will be delivered to your registered address')
                print('Please provide exact change to the delivery executive:')
                print('your estimated delivery will be in 5 days')
                print('Thanks for shopping!!')
                print()

                sqlp = "update products set quantity = quantity - 1 where name = '{}'".format(p_nm)

                try:

                    cur.execute(sqlp)
                    conn.commit()

                    print()
                    #print('Taking you to your home page:')
                    print()
                    # once done go back to home page

                    orr = input('Do you want to check your order? Y/N:')

                    if orr == 'Y':
                        self.track_order(pr_nm=p_nm, dt=da, c_nm=cu_nm, p_mo=py, amtt=amtt)

                    else:
                        ca = cart.Cart()
                        ca.clear_cart(c_usr)
                        c1 = customer.Customer()
                        c1.cus_home(c_usr)

                except Exception as e:
                    print(e)
                    conn.rollback()

            else:
                print('Invalid card no!')
                self.payment(p_nm, cu_nm, amtt, c_usr)

    def update_order(self, c_usr):

        global c1
        cur, conn = my_sql_conn.connect_to_db()
        print('What would you like to update?')
        print()
        print("1. Payment mode(only if you selected cod), type 'pay' ")
        print("2. Update Address, type 'up'")
        print("3. Replace and order something else, type 'rpl' ")
        print()
        oop = input('Enter your choice:')

        # update payment method to card

        if oop == 'pay':

            sq = "select payment_mode from orders where cuto_nm ='{}'".format(c_usr)

            cur.execute(sq)
            r = cur.fetchall()

            for k in r:
                if k[0] == 'cash':

                    # verify card no from customers table and the quantity should be reduced from products table
                    ca = int(input('Please enter your card number:'))
                    print('verifying the details please wait....')
                    print()
                    sql = "select * from customer"

                    cur.execute(sql)
                    result = cur.fetchall()

                    for i in result:
                        c1 = i[7]

                    if ca == c1:
                        # if card is valid place order
                        da = datetime.datetime.now()
                        da = da.strftime('%Y-%m-%d')
                        print('order updated successfully:', da)
                        print('Please provide exact change to the delivery executive:')
                        print('your estimated delivery will be in 5 days')
                        print('Thanks for shopping')
                        print()

                        # update the orders table
                        sql = "update orders set payment_mode = 'card' where cuto_nm = '{}'".format(c_usr)

                        try:
                            cur.execute(sql)
                            conn.commit()
                            print('Updated successfully')
                            print()
                            c = customer.Customer()
                            c.cus_home(c_usr)

                        except Exception as e:
                            print(e)
                            conn.rollback()

                    else:
                        print('Invalid card no')

                else:
                    print('looks like you already have payed by card')
                    print()
                    c = customer.Customer()
                    c.cus_home(c_usr)

        elif oop == 'up':

            nw_add = input('Enter your new city address:')

            sql = "update customer set address = '{}' where name = '{}'".format(nw_add, c_usr)

            try:
                cur.execute(sql)
                conn.commit()
                print('Address updated successfully going back to home!...')
                print()
                c = customer.Customer()
                c.cus_home(c_usr)

            except Exception as e:
                print(e)
                conn.rollback()

        elif oop == 'rpl':
            print("your current order will be deleted and you need to order a new product..")
            print()
            pdd = input('Do you want to continue? Y/N:')
            if pdd == 'Y' or pdd == 'y':
                self.cancel(c_usr)
                print('Order cancelled!')
                print()
            else:
                c = customer.Customer()
                c.cus_home(c_usr)

        else:
            c = customer.Customer()
            c.cus_home(c_usr)







