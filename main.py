from flask import Flask, render_template
from flask_mysqldb import MySQL

# configuracion con la base de datos
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'users'

#objeto de mysql
mysql = MySQL(app)
@app.route('/custumers', methods=['POST'])
def save_custumer():
    cur = mysql.connection.cursor()
    cur.execute('insert into customers values (%s)',
                (request.form['firstname'],))
    return "ok save"


@app.route('/custumers/<int:id>', methods=['DELETE'])
def remove_custumer(id):
    return "ok remove"


@app.route('/custumers/<int:id>')
def get_custumer(id):
    return "ok get"


@app.route('/custumers')
def get_all_custumer():
    return "ok get"


@app.route('/holaMundo')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(None, 8080, True)
