import pytest
from slack_utils import Event

event = Event({
    "type": "message",
    "user": "U12345",
    "channel": "C1234",
    "event_ts": "1234567890.123456",
    "thread_ts": "1234567890.123456",
    "text": "Hello world",
    "tab": "messages",
    "view": {
        "team": "T1234",
        "team_id": "T1234",
        "app_id": "A1234",
        "private_metadata": "some metadata"
    }
})

faulty_event = Event({})

def test_type():
    assert event.type == "message"

def test_no_type():
    assert faulty_event.type is None

def test_user_id():
    assert event.user_id == "U12345"

def test_no_user_id():
    assert faulty_event.user_id is None

def test_channel():
    assert event.channel == "C1234"

def test_no_channel():
    assert faulty_event.channel is None

def test_event_ts():
    assert event.event_ts == "1234567890.123456"

def test_no_event_ts():
    assert faulty_event.event_ts is None

def test_thread_ts():
    assert event.thread_ts == "1234567890.123456"

def test_no_thread_ts():
    assert faulty_event.thread_ts is None

def test_text():
    assert event.text == "Hello world"

def test_no_text():
    assert faulty_event.text is None

def test_tab():
    assert event.tab == "messages"

def test_no_tab():
    assert faulty_event.tab is None

def test_team():
    assert event.team == "T1234"

def test_no_team():
    assert faulty_event.team is None

def test_team_id():
    assert event.team_id == "T1234"

def test_no_team_id():
    assert faulty_event.team_id is None

def test_app_id():
    assert event.app_id == "A1234"

def test_no_app_id():
    assert faulty_event.app_id is None

def test_metadata():
    assert event.metadata == "some metadata"

def test_no_metadata():
    assert faulty_event.metadata is None
