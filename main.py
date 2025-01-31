from flask import Flask,render_template

app = Flask(__name__)

@app.route('/custumers',methods=['POST'])
def save_custumer():
    return "ok save"

@app.route('/custumers/<int:id>',methods=['DELETE'])
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
