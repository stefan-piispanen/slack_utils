import pytest
from slack_utils import Body

def test_user_id():
    body = Body({"user": {"id": "U12345"}})
    assert body.user_id == "U12345"

def test_user_id_missing():
    body = Body({})
    assert body.user_id is None

def test_view():
    body = Body({"view": {"view": {}}})
    assert isinstance(body.view, dict)

def test_no_view():
    body = Body({})
    assert body.view is None

def test_view_id():
    body = Body({"view": {"id": "1234"}})
    assert body.view_id == "1234"

def test_no_view_id():
    body = Body({})
    assert body.view_id is None
