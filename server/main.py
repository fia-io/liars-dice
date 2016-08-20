import flask
from flask import url_for
def fake_bid():
    pass

def fake_challenge():
    pass

def fake_get_status():
    pass

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def get_missing_json_params(json, required_params):
    missing_params = []
    for p in required_params:
        if json.get(p) is None:
            missing_params.append(p)
    return missing_params

@app.route('/play/game_status', methods=['GET'])
def game_status_get():
    missing_required_params = []
    for p in ['game_id', 'player_name']:
        if flask.request.args.get(p) is None:
            missing_required_params.append(p)
    
    if missing_required_params:
        return "Request was missing required URL parameters: '{0}'".format(
            "', '".join(missing_required_params))

    game_id = flask.request.args.get('game_id')
    player_name = flask.request.args.get('player_name')

    response = { 'game_id': game_id, 'player_name': player_name }
    return flask.jsonify(**response)

@app.route('/play/game_status', methods=['POST'])
def game_status_post():
    json = flask.request.get_json()
    if json is None:
        return flask.jsonify(**{'error': 'Request could not be parsed as JSON.'})

    missing_required_params = get_missing_json_params(
        json, ['game_id', 'player_name'])
    if missing_required_params:
        return flask.jsonify(**{
            'error': "Request was missing required JSON fields: '{0}'".format(
                "', '".join(missing_required_params))})
    
    game_id = json.get('game_id')
    player_name = json.get('player_name')

    response = { 'not implemented': 1 }
    return flask.jsonify(**response)

@app.route('/play/bid', methods=['POST'])
def bid():
    json = flask.request.get_json()
    if json is None:
        return flask.jsonify(**{'error': 'Request could not be parsed as JSON.'})

    missing_required_params = get_missing_json_params(
        json, ['game_id', 'round_number', 'player_name', 'bid_count', 'bid_die'])
    if missing_required_params:
        return flask.jsonify(**{
            'error': "Request was missing required JSON fields: '{0}'".format(
                "', '".join(missing_required_params))})
    
    game_id = json.get('game_id')
    round_number = json.get('round_number')
    player_name = json.get('player_name')
    bid_count = json.get('bid_count')
    bid_die = json.get('bid_die')

    response = { 'not implemented': 1 }
    return flask.jsonify(**response)

@app.route('/play/challenge', methods=['POST'])
def challenge():
    json = flask.request.get_json()
    if json is None:
        return flask.jsonify(**{'error': 'Request could not be parsed as JSON.'})

    missing_required_params = get_missing_json_params(
        json, ['game_id', 'round_number', 'player_name'])
    if missing_required_params:
        return flask.jsonify(**{
            'error': "Request was missing required JSON fields: '{0}'".format(
                "', '".join(missing_required_params))})

    game_id = json.get('game_id')
    round_number = json.get('round_number')
    player_name = json.get('player_name')

    response = { 'not implemented': 1 }
    return flask.jsonify(**response)

@app.route("/client")
def client():
   return flask.render_template('client.html')

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
    
