from xor_project import my_sql_conn
from xor_project import customer, admin
import pandas as pd
import keyboard


class Products:

    def get_details(self, nm):
        pass

    def view_product(self, c_usr):

        global db_name, df

        cur, conn = my_sql_conn.connect_to_db()

        sql = "select * from products"

        cur.execute(sql)

        result = cur.fetchall()

        df = pd.DataFrame(list(result), columns=['product_id', 'name', 'category', 'price', 'quantity', 'shipped', 'instock'])

        #for r in result:
            #df = pd.DataFrame([r],columns=['product_id','name','category','price','quantity','shipped','instock'])
            #print(r)

        print('Currently available items are:')
        print()
        print(df)
        print()
        print("please type 'b' to go the home page.")

        '''
        if db_name == nm:

            self.get_details(db_name)
            
        
            
        print()
        by = input("Type 'b' to go back to Home Page: ")
        if by == 'b' or by == 'B':
            cl = customer.Customer()
            cl.cus_home(c_usr)

        else:
            self.view_product()
        '''

    def v_p(self, c_usr):

        global db_name, df

        cur, conn = my_sql_conn.connect_to_db()

        sql = "select * from products"

        cur.execute(sql)

        result = cur.fetchall()

        df = pd.DataFrame(list(result),
                          columns=['product_id', 'name', 'category', 'price', 'quantity', 'shipped', 'instock'])

        # for r in result:
        # df = pd.DataFrame([r],columns=['product_id','name','category','price','quantity','shipped','instock'])
        # print(r)

        print('Currently available items are:')
        print()
        print(df)
        print()
        #print("please type 'b' to go the home page.")
        by = input("Type 'b' to go back to Home Page: ")
        if by == 'b' or by == 'B':
            cl = customer.Customer()
            cl.cus_home(c_usr)

        else:
            self.view_product()

    def add_product(self, tup):

        cur, conn = my_sql_conn.connect_to_db()

        sql = "insert into products(name,category,price,quantity, shipped,stock) values(%s,%s,%s,%s,%s,%r)"
        print(tup)
        try:
            cur.execute(sql, tup)
            conn.commit()
            print('Added successfully!')
            print()
        except Exception as e:
            print(e)
            cur.rollback()

    def remove_product(self):
        cur, conn = my_sql_conn.connect_to_db()

    def modify_p(self, db_nm):

        cur, conn = my_sql_conn.connect_to_db()

        sql = "select * from products"

        cur.execute(sql)

        result = cur.fetchall()

        df = pd.DataFrame(list(result), columns=['product_id', 'name', 'category', 'price', 'quantity', 'shipped', 'instock'])
        print(df)

        print()

        print("what would you like to modify?")
        print("Type 'name' for updating the name")
        print("Type 'category' for updating the name")
        print("Type 'price' for updating the name")
        print("Type 'quantity' for updating the name")
        print("Type 'ship' for updating the shipping company")
        print("Type 'stock' for updating the name")
        print("Type 'b' for to go back to home page")
        print()
        ch = input('Enter your choice separated by comma and product id:').split(',')
        print()

        if ch[0] == 'name':

            nw_nm = input('Enter new name for the product:')
            sql = "update products set name = '{}' where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product name updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'category':

            nw_nm = input('Enter new category name for the product:')
            sql = "update products set category = '{}' where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product  category name updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'price':

            nw_nm = int(input('Enter price for the product:'))
            sql = "update products set price = {} where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product price updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'quantity':

            nw_nm = int(input('Enter quantity for the product:'))
            sql = "update products set quantity = {} where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product quantity updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'stock':

            nw_nm = bool(input('Is the product in stock? true/false: '))
            sql = "update products set stock = '{}' where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product stock availability updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'ship':

            nw_nm = input('Enter the new shipping company: ')
            sql = "update products set shipped = '{}' where product_id = {}".format(nw_nm, ch[1])

            try:
                cur.execute(sql)
                conn.commit()
                print('Product shipping company updated successfully')
                print()
                self.modify_p()

            except Exception as e:
                print(e)
                conn.rollback()
                self.modify_p()

        elif ch[0] == 'b':
            aa = admin.Admin()
            aa.admin_menu(db_nm)















