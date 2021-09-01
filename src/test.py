import pymysql
from app import app
from flask import jsonify
from flask import flash, request

@app.route('/pending')
def pending():
    try:
        conn = pymysql.connect(
        host="10.147.18.185",
        user="k3s",
        password="k3s_123",
        database="rm"
        )
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT `id`, `package`, `system`, `baseline`, `state`, `dimstream` FROM `pending-packages`")
        rows = cur.fetchall()
        resp=jsonify(rows)
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        
if __name__ == "__main__":
    app.run()