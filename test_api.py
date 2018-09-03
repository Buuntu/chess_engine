import os
import tempfile
import json
import chess

import pytest

from server import app

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

def test_new_game(client):
    response = client.get('/new_game')
    json_response = json_of_response(response)
    assert json_response['board'] == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    assert response.status_code == 200

def test_move(client):
    response = post_json(client, '/random_move', {'board': chess.Board().fen()})
    json_response = json_of_response(response)
    assert len(json_response['board']) > 30
    assert response.status_code == 200

