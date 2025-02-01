from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

# configuracion con la base de datos
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'users_bd'

# objeto de mysql
mysql = MySQL(app)


@app.route('/custumers', methods=['POST'])
def save_custumer():
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO custumers (firstname, lastname, email, phone, address) VALUES ('Jhonatan', 'Ojeda Sanchez', 'jhona@gmail.com', '963258741', 'Peru')")
    mysql.connection.commit()
    return "ok save custumer"


@app.route('/custumers/<int:id>', methods=['DELETE'])
def remove_custumer(id):
    cur = mysql.connection.cursor()
    cur.execute(
        "DELETE FROM custumers WHERE custumer_id = %s", )
    mysql.connection.commit()
    return "ok remove custumer by id ", id


@app.route('/custumers/<int:id>')
def get_custumer(id):
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT custumer_id,firstname,lastname,email,phone, address FROM custumers WHERE custumer_id = " + str(id))
    row = cur.fetchone()
    content = {"custumer_id": row[0],
               "firstname": row[1],
               "lastname": row[2],
               "email": row[3],
               "phone": row[4],
               "address": row[5]}
    return jsonify(content)


@app.route('/custumers')
def get_all_custumer():
    cur = mysql.connection.cursor()
    cur.execute("SELECT custumer_id,firstname,lastname,email,phone, address FROM custumers")
    data = cur.fetchall()
    result = []
    for row in data:
        content = {
            "custumer_id": row[0],
            "firstname": row[1],
            "lastname": row[2],
            "email": row[3],
            "phone": row[4],
            "address": row[5],
        }
        result.append(content)
    return jsonify(result)


@app.route('/holaMundo')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(None, 8080, True)
