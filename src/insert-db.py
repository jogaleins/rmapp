import mysql.connector

def connectdb():
    mydb = mysql.connector.connect(
    host="10.147.18.185",
    user="k3s",
    password="k3s_123",
    database="rm"
    )
    return mydb
def truncate():
    mydb = connectdb()
    mycursor = mydb.cursor()
    mycursor.execute("TRUNCATE TABLE `pending-packages`")
    mydb.commit()
    mydb.close()

def insert():
    mydb = connectdb()

    mycursor = mydb.cursor()

    sql = "INSERT INTO `pending-packages` (`id`, `package`, `system`, `baseline`, `state`, `dimstream`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [
    (1, 'Sideway 1633','11','232','adsfasdf','asdfasdfa')
    ]

    mycursor.executemany(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "was inserted.")
    mydb.close()

def select():
    print('test select')
    mydb = connectdb()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `pending-packages`")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()

def main():
    truncate()
    insert()
    select()

main()