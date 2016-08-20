import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)

@app.route("/base")
def base_template():
    return flask.render_template('base.html')

@app.route("/json_test")
def json_test():
    d = {'a': 4, 'b': 9}
    return flask.jsonify(**d)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
