function mbar_test() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/play/game_status");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify({game_id: 7, other: 3}));
}

function mbar_test_challenge() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/play/challenge");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify({game_id: 7, round_number: 3, player: 'you'}));
}

function mbar_test_broken_challenge() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/play/challenge");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify({game_id: 7, player: 'you'}));
}

function mbar_test_super_broken_challenge() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/play/challenge");
    xmlhttp.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    xmlhttp.send("Totally not JSON.");
}

function mbar_test_incomplete_bid() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/play/bid");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify({game_id: 7, player: 'you'}));
}
