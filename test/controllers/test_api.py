import pytest
from src.app import create_app


@pytest.fixture
def app():
    return create_app()


def test_health(app):
    response = app.test_client().get('/api/health')
    assert response.json['message'] == "Server is healthy"


def test_should_add_comment_to_topic(app):
    "It should add comment to given topic id"

    body = {
        'comment': 'This is a very informative blog. I would suggest ...',
        'topic-id': 'getting-started-with-docker'
    }

    expected_response = {
        "topic-id": "getting-started-with-docker",
        "comment-id": '1',
        "total-comments": 1
    }

    response = app.test_client().post('/api/add-comment', json=body)
    assert response.json == expected_response


# @pytest.mark.only
# def test_should_response_comments_of_given_topic(app):
#     "It should response comments of given topic"

#     client = app.test_client()

#     comment = {
#         'comment': 'This is a very informative blog. I would suggest ...',
#         'topic-id': 'getting-started-with-docker'
#     }

#     client.post('/api/add-comment', json=comment)

#     topic_id = 'getting-started-with-docker'

#     expected_comments = [
#         {
#             'comment': 'This is a very informative blog. I would suggest ...',
#             'topic-id': 'getting-started-with-docker'
#         }
#     ]

#     response = client.get('/api/comments/'+topic_id)
#     assert response.json == expected_comments
