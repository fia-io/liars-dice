import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/play/game_status', methods=['GET','POST'])
def game_status():
    response = {}
    print(str(flask.request.json))
    print(str(flask.request.get_json()))
    if flask.request.json:
        request_data = flask.request.json
        response['game_id'] = request_data.get('game_id')

    print(str(response))
    return flask.jsonify(**response)

@app.route('/play/bid', methods=['POST'])
def bid():
    return 'I should totally return a bid here.'

@app.route('/play/challenge', methods=['POST'])
def challenge():
    return 'I should totally return a challenge here.'



@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)

@app.route("/json-upload", methods=['GET','POST'])
def json():
    
    #print(str(flask.request.json))
    
    if flask.request.json:
        mydata = flask.request.json # will be 
        
        return "Thanks. Your age is %s" % mydata.get("age")

    else:
        return "no json received"

@app.route("/base")
def base_template():
    return flask.render_template('base.html')

@app.route("/json_test")
def json_test():
    d = {'a': 4, 'b': 9}
    return flask.jsonify(**d)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
