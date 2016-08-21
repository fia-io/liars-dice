import flask
import engine

# HACK: Create a single game in th engine with known players and known dice
e = engine.Engine(None)
e.create_game(['me', 'you'], 3)
e.set_dice(1, 0, 'me', [5, 5, 6])
e.set_dice(1, 0, 'you', [3, 3, 4])
print(e.game_status(1, 'me'))
print(e.game_status(1, 'you'))


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

def parse_status(status):
    gi, gs, rn, pt, d, b = status
    
    bidder, num_dice, die_face = b[-1]
    
    bid_string = "{0} x {1}'s".format(num_dice, die_face)

    response = {
        'game_id': gi,
        'game_state': gs,
        'round_number': rn,
        'player_turn': pt,
        'dice': d,
        'bid': bid_string
    }
    
    return response

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

    status = e.game_status(int(game_id), player_name)

    #gi, gs, rn, pt, d, b = status
    
    #bidder, num_dice, die_face = b[-1]
    
    #bid_string = "{0} x {1}'s".format(num_dice, die_face)

    #response = {
    #    'game_id': gi,
    #    'game_state': gs,
    #    'round_number': rn,
    #    'player_turn': pt,
    #    'dice': d,
    #    'bid': bid_string
    #}
    
    response = parse_status(status)
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

    response = parse_status(e.game_status(int(game_id), player_name))
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

    #response = { 'game_id' : game_id, 'round_number': round_number, 'player_name' : player_name, 'bid_count' : bid_count, 'bid_die' : bid_die};
    response = { 'game_id': game_id, 'player_name': player_name }
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

    #response = { 'game_id' : game_id, 'round_number' : round_number, 'player_name' : player_name };
    response = { 'game_id': game_id, 'player_name': player_name }
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
