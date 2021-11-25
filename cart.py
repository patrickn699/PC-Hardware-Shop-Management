from xor_project import my_sql_conn
from xor_project import order, customer
import pandas as pd


class Cart:

    def add_product(self, pr_nm, qty, id):

        global i1, n1, i2, i3

        cur, conn = my_sql_conn.connect_to_db()

        sql1 = "select * from products"
        sql2 = "insert into cart(cust_nm,product_nm,product_cat,quantity,price) values(%s,%s,%s,%s,%s)"
        sql3 = "select name from customer where id = {}".format(id)

        cur.execute(sql1)

        result = cur.fetchall()

        # for getting product name, category, price
        for i in result:
            if i[1] == pr_nm:
                print(i[1], i[2], i[3])
                i1 = i[1]
                i2 = i[2]
                i3 = i[3]

        # for getting user name
        cur.execute(sql3)
        r2 = cur.fetchall()

        for j in r2:
            n1 = j[0]

        # for inserting into cart

        tup = (n1, i1, i2, qty, i3)
        try:
            cur.execute(sql2, tup)
            conn.commit()
            print('Your product has been added to the cart!')
            print()
        except Exception as e:
            print(e)

            conn.rollback()

    def remove_product(self, c_usr):
        # method to remove the product from cart
        cur, conn = my_sql_conn.connect_to_db()
        sql1 = "select * from cart"

        print('Your cart items are:')
        print()

        print('id', 'Product name', 'Product category', 'Quantity', 'Price')
        cur.execute(sql1)
        res = cur.fetchall()
        '''
        for i in res:
            print(i)
        '''
        df = pd.DataFrame(list(res), columns=['Id', 'Customer name', 'Product name', ' Product category', 'Quantity', 'Price'])
        print(df)
        print()

        i_nm = input("Enter product id  that you want to remove or type 'b' to go back:")
        sql = "delete from cart where id = {}".format(i_nm)
        if i_nm != 'b':
            try:
                cur.execute(sql)
                conn.commit()

                print("product removed from cart successfully!")
                cc = customer.Customer()
                cc.cus_home()
            except Exception as e:
                print(e)
                conn.rollback()
                cc1 = customer.Customer()
                cc1.cus_home(c_usr)
        else:
            cc1 = customer.Customer()
            cc1.cus_home(c_usr)

    def view_cart(self, p_nm, c_usr):

        global qn, pri
        pri = 0

        cur, conn = my_sql_conn.connect_to_db()

        sql = "select * from cart"

        cur.execute(sql)

        result = cur.fetchall()

        # for printing the cart
        '''
        for i in result:
            print(i)
        '''
        df = pd.DataFrame(list(result), columns=['Id', 'Customer name', 'Product name', ' Product category', 'Quantity', 'Price'])
        print(df)
        # order total amount

        for j in result:
            qn = j[4]
            pri += j[5]*qn
        print()
        print('Your order total is:', pri)
        print()
        # for checkout
        
        if pri !=0:
            ck = input('Do you want to checkout? Y/N:')
            print()
    
            if ck == 'Y':
                o1 = order.Order()
                o1.payment(p_nm, cu_nm=c_usr, amtt = pri, c_usr=c_usr)
                self.clear_cart(c_usr)
    
            else:
                # go back to home page of customer
                cc = customer.Customer()
                cc.cus_home(c_usr)
        else:
            bak = input("Press 'b' to go back:")
            if bak == 'b':
                cr = customer.Customer()
                cr.cus_home(c_usr)

    def clear_cart(self, c_nm):

        # clearing cart once checked out
        cur, conn = my_sql_conn.connect_to_db()
        #print('in clear', c_nm)

        sql = "delete from cart where cust_nm = '{}'".format(c_nm)

        try:
            cur.execute(sql)
            conn.commit()
            print('Your cart is now empty!')

        except Exception as e:
            print(e)
            conn.rollback()



