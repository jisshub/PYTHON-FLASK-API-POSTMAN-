from flask import Flask, request, jsonify

# create instance of Flask object
app = Flask(__name__)

# define a route endpoint as /xyz
@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        a = request.json['NUM1']
        b = request.json['NUM2']
        result = a + b
    # return JSON with message
    return jsonify(str(result))

# define a new route with different endpoint
@app.route('/abc', methods=['POST'])
def test1():
    if request.method == 'POST':
        a = request.json['NUM3']
        b = request.json['NUM4']
        result = a + b
    return jsonify(str(result))

if __name__ == '__main__':
    # run the app
    app.run()
