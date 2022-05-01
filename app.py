from flask import Flask, jsonify, request, escape
 
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    msg = {'message': 'success'}
    return jsonify(msg)


@app.route('/config', methods=['POST'])
def getData():
    data = request.json
    version = escape(data.get('version', None))
    if not version:
        msg = {'message': 'bad request'}
        return jsonify(msg), 400
    msg = {'message': 'success', 'data': data}
    return jsonify(msg)

# app.add_url_rule("/", view_func=main, methods=['GET'])

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)