from flask import Flask, request, jsonify
from flask_cors import CORS

import modelTitanic

'''
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
    
'''
app = Flask(__name__)
CORS(app)


@app.route('/survie/<int:pclass>/<int:sex>/<int:age>', methods=['GET'])
def survie(pclass, sex, age):
    return modelTitanic.survie(pclass, sex, age)

# @app.route('/')
# def hello_world():
#     titanic = pd.read_excel("static/dataset/titanic_.xls")
#     # Convert the DataFrame to a JSON string and return it
#     titanic_json = titanic.head().to_json(orient='records')
#     return titanic_json


@app.route('/')
def hello_world():
    return "Hello World !"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
