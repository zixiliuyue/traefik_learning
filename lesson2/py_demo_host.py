from flask import Flask

app = Flask(__name__)

@app.route('/host')
def hello():
    return 'host!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8864)
