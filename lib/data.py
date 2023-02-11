import MySQLdb

# 创建一个 Connection 对象，代表了一个数据库连接
connection = MySQLdb.connect(
                host="localhost",# 数据库IP地址
                user="user01",     #  mysql用户名
                passwd="admin",      # mysql用户登录密码
                db="dev_test" ,        # 数据库名
                # 如果数据库里面的文本是utf8编码的，
                #charset指定是utf8
                charset = "utf8")

# 返回一个 Cursor对象
c = connection.cursor()

# 执行一个获取 users 表中所有记录的 sql 语句
c.execute("")


# rowcount属性记录了最近一次 execute 方法获取的数据行数
numrows = c.rowcount

connection.commit()

connection.close()