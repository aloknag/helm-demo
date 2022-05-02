from flask import Flask, jsonify, request, escape
 
app = Flask(__name__)

version = None    

@app.route('/', methods=['GET'])
def main():
    msg = {'message': 'success'}
    return jsonify(msg)



@app.route('/config', methods=['GET', 'POST'])
def getData():
    global version
    if request.method == 'POST':
        data = request.json
        v = data.get('version', None)
        if not v:
            msg = {'message': 'bad request'}
            return jsonify(msg), 400
        version = v
        msg = {'message': 'success', 'version': version}
        return jsonify(msg)
    elif request.method == 'GET':
        msg = {'message': 'success', 'version': version}
        return jsonify(msg)

# app.add_url_rule("/", view_func=main, methods=['GET'])

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)