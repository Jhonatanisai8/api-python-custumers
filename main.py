from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# configuracion con la base de datos
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'users_bd'

# objeto de mysql
mysql = MySQL(app)


@app.route('/api/custumers', methods=['POST'])
@cross_origin() # para que se llame desde puertos diferentes
def save_custumer():
    # return request.json['firstname']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO custumers (firstname, lastname, email, phone, address) VALUES (%s, %s, %s, %s, %s);"
        , (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'],
           request.json['address']))
    mysql.connection.commit()
    return "Custumers saved"


@app.route('/api/custumers', methods=['PUT'])
@cross_origin() # para que se llame desde puertos diferentes
def update_custumer():
    # return request.json['firstname']
    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE custumers SET firstname = %s, lastname = %s, email = %s, phone = %s, address = %s WHERE custumer_id = %s;"
        , (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'],
           request.json['address'], request.json['custumer_id']))
    mysql.connection.commit()
    return "Custumers update"


@app.route('/api/custumers/<int:id>', methods=['DELETE'])
@cross_origin() # para que se llame desde puertos diferentes
def remove_custumer(id):
    cur = mysql.connection.cursor()
    cur.execute(
        "DELETE FROM custumers WHERE custumer_id = %s", )
    mysql.connection.commit()
    return "ok remove custumer by id ", id


@app.route('/api/custumers/<int:id>')
@cross_origin() # para que se llame desde puertos diferentes
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


@app.route('/api/custumers')
@cross_origin() # para que se llame desde puertos diferentes
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
@cross_origin() # para que se llame desde puertos diferentes
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(None, 8080, True)
