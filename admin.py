from xor_project import my_sql_conn
from xor_project import products
import pandas as pd


class Admin:

    def login(self):

        global db_pass, db_name

        print()

        db_aname = input('Enter your name:')

        db_apass = input('Enter your password:')

        cur, conn = my_sql_conn.connect_to_db()

        sql = ' select * from admin'

        cur.execute(sql)

        result = cur.fetchall()

        for r in result:
            db_name = r[1]
            db_pass = r[2]

        if db_aname == db_name and db_apass == db_pass:
            #print('Welcome Admin!')
            return db_name
        
        else:
            print('Incorrect login credentials...please try again!')
            self.admin_menu()

    def add_p(self, db_name):

        global no
        no = 'Y'
        while no == 'Y':
            print('Enter the product you want to add in the following order:')
            print('Name, Category, Price, Quantity, Shipping, Stock')
            print()
            to_add = input('Enter the product details:').split(',')
            to_add[2] = int(to_add[2])
            to_add[3] = int(to_add[3])
            to_add[5] = bool(to_add[5])
            tod_add = tuple(to_add)
            print('You have entered the following details:', tod_add)
            p = products.Products()
            p.add_product(tod_add)
            no = input('Do you want to add another? Y/N:')

            if no == 'N':
                self.admin_menu(db_name)

    def admin_menu(self, db_name):

        print('Welcome,', db_name)
        print()
        print('What would you like to do?')
        print()
        print("1. Type 'add' to add new product")
        print("2. Type 'remove' to remove product")
        print("3. Type 'view' to view product")
        print("4. Type 'modify' to modify product")
        print()
        res = input('Enter your choice:')

        if res == 'Add' or res == 'add':
            self.add_p(db_name=db_name)

        elif res == 'Remove' or res == 'remove':
            self.remove_p(db_name)

        elif res == 'View' or res == 'view':
            self.view(db_name)
            
        elif res == 'modify':
            pp = products.Products()
            pp.modify_p(db_name)
            
        else:
            self.admin_menu(db_name)

    def remove_p(self, db_name):

        cur, conn = my_sql_conn.connect_to_db()
        sql1 = "select * from products"

        #print('id', 'Product name', 'Product category', 'Price', 'Quantity', 'Shipped', 'Stock')
        cur.execute(sql1)
        res = cur.fetchall()

        df = pd.DataFrame(list(res), columns=['Id', 'Product name', ' Product category', 'Price', 'quantity', 'Shipped', 'Stock'])
        '''
        for i in res:
            print(i)
        '''
        print(df)
        print()


        a_rm = int(input('Enter the id of the product to remove:'))

        sql = "delete from products where product_id={}".format(a_rm)

        try:
            cur.execute(sql)
            conn.commit()
            print("Product removed successfully!")
            self.admin_menu(db_name)

        except Exception as e:
            print(e)
            conn.rollback()

    def view(self, db_name):
        cur, conn = my_sql_conn.connect_to_db()

        sql = "select * from products"

        cur.execute(sql)

        result = cur.fetchall()
        '''
        print('id', 'Product name', 'Product category', 'Price', 'Quantity', 'Shipped', 'Stock')
        for i in result:
            print(i)
        '''

        df = pd.DataFrame(list(result), columns=['Id', 'Product name', ' Product category', 'Price', 'quantity', 'Shipped', 'Stock'])

        print(df)
        print()

        hp = input("Type 'b' to go to home page:")

        if hp == 'b':
            self.admin_menu(db_name)

        else:
            self.view()






