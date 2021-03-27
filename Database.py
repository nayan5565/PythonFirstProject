import mysql.connector
import pymysql

my_db = mysql.connector.connect(host='localhost', user='nayan', password='1234', database='bristy')

my_cursor = my_db.cursor()

my_cursor.execute('select * from student')

result = my_cursor.fetchone()

for i in result:
    print(i)

# pymsql

host = 'test-db-instance.czrrnivxlbjc.us-west-2.rds.amazonaws.com'
connection = pymysql.connect(host=host, user='admin', password='asd123456', database='test_db', connect_timeout=5)
connection.begin()

try:
    with connection.cursor() as cur:
        cur.execute("select * from test_table")
    employee_result = cur.fetchall()
    print('result: ', employee_result)

    connection.commit()

except Exception as e:
    print(e)
