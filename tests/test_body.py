import pytest
from slack_utils import Body

body = Body({
        "user": {"id": "U12345"},
        "view": {
            "view": {},
            "id": "1234",
            "blocks": []
            },
        "trigger_id": "1234",
        })

faulty_body = Body({
        })

def test_user_id():
    assert body.user_id == "U12345"

def test_user_id_missing():
    assert faulty_body.user_id is None

def test_view():
    assert isinstance(body.view, dict)

def test_no_view():
    assert faulty_body.view is None

def test_view_id():
    assert body.view_id == "1234"

def test_no_view_id():
    assert faulty_body.view_id is None

def test_trigger_id():
    assert body.trigger_id == "1234"

def test_no_trigger_id():
    assert faulty_body.trigger_id is None

def test_blocks():
    assert isinstance(body.blocks, list)

def test_no_blocks():
    assert faulty_body.blocks is None
