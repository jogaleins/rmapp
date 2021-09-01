import mysql.connector
import json
from flask import Flask
from flask import jsonify


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

def returnpackagelist():
    mydb = connectdb()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT `id`, `package`, `system`, `baseline`, `state`, `dimstream` FROM `pending-packages`")

    myresult = mycursor.fetchall()
    row_headers=[x[0] for x in mycursor.description] 

    mydb.close()
    json_data=[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)
    #return jsonify(json_data)

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
    #truncate()
    #with open('json/pending-packages.json', 'r') as f:
    #    packages = json.load(f)
    #    insert_packages(packages)
    #test()
    print(returnpackagelist())
    #select()

main()