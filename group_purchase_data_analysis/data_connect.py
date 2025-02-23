import pymysql

def get_mysql_connection() -> object:
    # 连接到 MySQL 数据库
    connection = pymysql.connect(
        host='127.0.0.1',
        database='shop',
        user='root',
        password=''
    )

    if connection.open:
        print("成功连接到 MySQL 数据库")
        return connection
    else:
        print('MYSQL 连接异常')
