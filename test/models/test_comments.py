import pytest
from src.models.Comment import Comment
from src.models.Comments import Comments


def test_should_add_one_comment():
    "should add one comment to given topic"
    # GIVEN
    id = '2323424'
    message = 'This is some useful message. This is important'
    username = 'anonymous'
    avatar = 'someurl'

    comment = Comment(id, message, username, avatar)

    comments = Comments()

    topic_id = 'docker-image-layers'
    expected_total_comments = 1

    # WHEN
    actual_total_comments = comments.add(comment, topic_id)

    # THEN
    assert actual_total_comments == expected_total_comments


def test_should_add_multiple_comments():
    # GIVEN
    id1 = '2323424'
    message1 = 'This is some useful message. This is important'
    username1 = 'anonymous'
    avatar1 = 'someurl'

    comment1 = Comment(id1, message1, username1, avatar1)

    id2 = '2323424'
    message2 = 'This is some useful message. This is important'
    username2 = 'anonymous'
    avatar2 = 'someurl'

    comment2 = Comment(id2, message2, username2, avatar2)

    comments = Comments()

    topic_id = 'docker-image-layers'
    expected_total_comments = 2

    # WHEN
    comments.add(comment1, topic_id)
    actual_total_comments = comments.add(comment2, topic_id)

    # THEN
    assert actual_total_comments == expected_total_comments


def test_should_add_one_comments_multiple_topics():
    # GIVEN
    id1 = '2323424'
    message1 = 'This is some useful message. This is important'
    username1 = 'anonymous'
    avatar1 = 'someurl'

    comment1 = Comment(id1, message1, username1, avatar1)

    id2 = '2323424'
    message2 = 'This is some useful message. This is important'
    username2 = 'anonymous'
    avatar2 = 'someurl'

    comment2 = Comment(id2, message2, username2, avatar2)

    comments = Comments()

    topic_id_1 = 'docker-image-layers'
    topic_id_2 = 'docker-volume'

    expected_topic_1_total_comments = 1
    expected_topic_2_total_comments = 1

    # WHEN
    actual_topic_1_total_comments = comments.add(comment1, topic_id_1)
    actual_topic_2_total_comments = comments.add(comment2, topic_id_2)

    # THEN
    assert actual_topic_1_total_comments == expected_topic_1_total_comments
    assert actual_topic_2_total_comments == expected_topic_2_total_comments


def test_should_retrieve_topic_id_comments():
    "It should retrieve all the comments added for the given topic"

    id1 = '2323424'
    message1 = 'This is some useful message. This is important'
    username1 = 'anonymous'
    avatar1 = 'someurl'

    comment1 = Comment(id1, message1, username1, avatar1)

    id2 = '2323424'
    message2 = 'This is some useful message. This is important'
    username2 = 'anonymous'
    avatar2 = 'someurl'

    comment2 = Comment(id2, message2, username2, avatar2)

    comments = Comments()

    topic_id = 'docker-image-layers'

    expected_comments = [comment2, comment1]

    comments.add(comment1, topic_id)
    comments.add(comment2, topic_id)

    actual_comments = comments.getAll(topic_id)

    assert actual_comments == expected_comments


def test_should_retrieve_empty_comments_of_topic_id():
    "It should retrieve no comments of topic id when no comments added"

    comments = Comments()

    topic_id = 'docker-image-layers'

    expected_comments = []

    actual_comments = comments.getAll(topic_id)

    assert actual_comments == expected_comments
