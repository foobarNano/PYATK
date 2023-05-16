import mysql.connector

def connect():
    f = open("./C10/acc.txt", "r")
    lines = f.readlines()
    conn = mysql.connector.connect(
        host=lines[0].rstrip(),
        user=lines[1].rstrip(),
        password=lines[2].rstrip(),
        database=lines[3].rstrip()
    )
    f.close()
    return conn

def fetch():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select * from books")
    result = cursor.fetchall()
    cursor.close()
    conn.cursor()
    return result

def insert(data: tuple = None):
    conn = connect()
    cursor = conn.cursor()
    # cursor.execute("insert into books values ")
    cursor.execute("insert into books values (4, 'test', 'test', 10.0, 'None')")
    conn.commit()
    cursor.close()
    conn.cursor()



insert()
print(fetch())