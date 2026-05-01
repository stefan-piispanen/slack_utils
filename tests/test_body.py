import pytest
from slack_utils import Body

def test_user_id():
    body = Body({"user": {"id": "U12345"}})
    assert body.user_id == "U12345"

def test_user_id_missing():
    body = Body({})
    assert body.user_id is None
