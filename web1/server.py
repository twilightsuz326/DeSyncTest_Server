from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # the next line is required for Transfer-Encoding support in the request
    request.environ['wsgi.input_terminated'] = True
    headers = {}
    for header in request.headers:
        headers[header[0]] = header[1]

    body = None
    if request.method == 'POST':
        body = request.get_data(as_text=True)

    # ヘッダーとボディを返す
    return jsonify({
        'Method': request.method,
        'headers': headers,
        'params': request.args,
        'body': body,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
