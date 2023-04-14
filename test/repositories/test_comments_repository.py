"test_comments_repository.py"
from urllib import response
import pytest
from src.models.Comment import Comment
from src.repositories.comments_repository import CommentsRepository
from src.stores.store import Store

from src.stores.memory_store import MemoryStore


@pytest.fixture
def store():
    return MemoryStore()


@pytest.mark.only
async def test_should_add_comment_to_store(store):
    "It should add a comment to store"

    repository = CommentsRepository(store)
    expected_total_comments = 1

    actual_total_comments = await repository.add(
        Comment('1', 'hey there', 'user', 'url', 'docker')
    )

    assert actual_total_comments == expected_total_comments


@pytest.mark.only
async def test_should_add_comment_to_filled_store(store: Store):
    "It should add a comment to already filled store"

    await store.insert('comments', Comment('1', 'hello', 'user', 'url', 'docker'))
    # store.put('comments', {'docker': []})

    repository = CommentsRepository(store)
    expected_total_comments = 2

    actual_total_comments = await repository.add(
        Comment('1', 'hey there', 'user', 'url', 'docker')
    )

    assert actual_total_comments == expected_total_comments


@pytest.mark.only
async def test_should_get_comment_from_store(store: Store):
    "It should get a comment from the store"

    await store.insert('comments', Comment('1', 'hello', 'user', 'url', 'docker'))
    repository = CommentsRepository(store)
    expected_comments = [Comment('1', 'hello', 'user', 'url', 'docker')]

    actual_comments = await repository.get('docker')

    assert expected_comments == actual_comments


@pytest.mark.only
async def test_should_get_comment_from_empty_store(store: Store):
    "It should get a comment from empty store"

    repository = CommentsRepository(store)
    expected_comments = []

    actual_comments = await repository.get('docker')

    assert expected_comments == actual_comments
