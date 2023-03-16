import json
from src.app import create_app

app = create_app()


def test_health():
    response = app.test_client().get('/api/health')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) == dict
    assert res['message'] == "Server is healthy"
