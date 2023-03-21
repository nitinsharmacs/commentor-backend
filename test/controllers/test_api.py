from datetime import datetime
import pytest
from src.app import create_app
from src.controllers.api import comments
from src.models.Map import Map


@pytest.fixture
def app():
    yield create_app().test_client()
    comments.clear()


def test_health(app):
    response = app.get('/api/health')
    assert response.json['message'] == "Server is healthy"


@pytest.mark.only
def test_should_add_comment_to_topic(app):
    "It should add comment to given topic id"

    body = {
        'comment': 'It is a cool ...',
        'topic-id': 'getting-started-with-docker'
    }

    expected_response = {
        "topic-id": "getting-started-with-docker",
        "comment-id": '1',
        "total-comments": 1
    }

    response = app.post('/api/add-comment', json=body)
    assert response.json == expected_response


@pytest.mark.only
def test_should_response_comments_of_given_topic(app):
    "It should response comments of given topic"

    client = app

    comment = {
        'comment': 'This is a very informative blog. I would suggest ...',
        'topic-id': 'getting-started-with-docker'
    }

    client.post('/api/add-comment', json=comment)

    topic_id = 'getting-started-with-docker'

    expected_comments = {
        'topic-id': topic_id,
        'comments': [
            {
                'message': 'This is a very informative blog. I would suggest ...',
                'topic-id': 'getting-started-with-docker',
                'id': '1',
                'avatar': 'some_url',
                'likes': 0,
                'username': 'anonymous',
            }
        ]
    }

    response = client.get('/api/comments/'+topic_id).json
    assert response['topic-id'] == topic_id
    assert len(response['comments']) == 1
