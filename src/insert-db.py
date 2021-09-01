import mysql.connector
import json

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
    print('table truncated')

def select():
    print('show records')
    mydb = connectdb()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `pending-packages`")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mydb.close()
def insert_packages(packages):
    try:
        mydb = connectdb()
        mycursor = mydb.cursor()
        mycursor.executemany("""
        INSERT INTO `pending-packages` (`id`, `package`, `system`, `baseline`, `state`, `dimstream`)
        VALUES (%(ID)s, %(PACKAGE)s,%(SYSTEM)s, %(BASELINE)s,%(STATE)s, %(DIMSTREAM)s)""", packages)
        mydb.commit()

    except Error as e:
        print('Error:', e)

    finally:
        mycursor.close()
        mydb.close()
        print('records inserted')

def main():
    truncate()
    with open('json/pending-packages.json', 'r') as f:
        packages = json.load(f)
        insert_packages(packages)
    #test()
    select()

main()