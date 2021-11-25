import pymysql


def connect_to_db():
    connection = pymysql.connect(host='localhost', user='root', password='admin', db='order_m')
    print('connected')
    cursor = connection.cursor()
    return cursor, connection
