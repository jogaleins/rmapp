from flask import Flask
from Flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    returnpackagelist()


def connectdb():
    mydb = mysql.connector.connect(
    host="10.147.18.185",
    user="k3s",
    password="k3s_123",
    database="rm"
    )
    return mydb

def returnpackagelist():
    mydb = connectdb()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `pending-packages`")

    myresult = mycursor.fetchall()
    mydb.close()
    return myresult.json_encoder()

    

if __name__ == "__main__":
    app.run()