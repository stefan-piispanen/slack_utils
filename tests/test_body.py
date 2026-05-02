import pytest
from slack_utils import Body

body = Body({
        "user": {
            "id": "U12345",
            "team_id": "1234",
            "name": "Test",
            "username": "Test"
            },
        "view": {
            "view": {},
            "id": "1234",
            "blocks": [],
            "bot_id": "1234",
            "private_metadata": {},
            "state": {
                "values": {
                    "datepicker_id": {
                        "datepicker_id": {
                            "type": "datepicker",
                            "selected_date": "2026-01-01"
                            }
                        },
                    "plain_text_id": {
                        "plain_text_id": {
                            "type": "plain_text_input",
                            "value": "test_text"
                            }
                        },
                    "static_id": {
                        "static_id": {
                            "type": "static_select",
                            "selected_option": {
                                "value": "test_value"
                                }
                            }
                        }
                    }
                }
            },
        "trigger_id": "1234",
        "team": {
            "domain": "1234",
            "id": "1234"
            },
        "channel": {
            "id": "C1234"
            },
        "container": {},
        "actions": [{"value": "{}"}],
        "message": {}
        })

faulty_body = Body({
        })

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

def test_bot_id():
    assert body.bot_id == "1234"

def test_no_bot_id():
    assert faulty_body.bot_id is None

def test_private_metadata():
    assert isinstance(body.private_metadata, dict)

def test_no_private_metadata():
    assert faulty_body.private_metadata is None

def test_team_domain():
    assert body.team_domain == "1234"

def test_no_team_domain():
    assert faulty_body.team_domain is None

def test_team_id():
    assert body.team_id == "1234"

def test_team_id_missing():
    assert faulty_body.team_id is None

def test_user_id():
    assert body.user_id == "U12345"

def test_user_id_missing():
    assert faulty_body.user_id is None

def test_user_team_id():
    assert body.user_team_id == "1234"

def test_no_user_team_id():
    assert faulty_body.user_team_id is None

def test_name():
    assert body.name == "Test"

def test_no_name():
    assert faulty_body.name is None

def test_user_name():
    assert body.user_name == "Test"

def test_no_user_name():
    assert faulty_body.user_name is None

def test_channel_id():
    assert body.channel_id == "C1234"

def test_no_channel_id():
    assert faulty_body.channel_id is None

def test_values():
    assert isinstance(body.values, dict)

def test_no_values():
    assert faulty_body.values is None

def test_container():
    assert isinstance(body.container, dict)

def test_no_container():
    assert faulty_body.container is None

def test_actions():
    assert isinstance(body.actions, dict)

def test_no_actions():
    assert faulty_body.actions is None

def test_value():
    assert isinstance(body.value, dict)

def test_no_value():
    assert faulty_body.value is None

def test_message():
    assert isinstance(body.message, dict)

def test_no_message():
    assert faulty_body.message is None

def test_get_value_datepicker():
    assert body.get_value("datepicker_id") == "2026-01-01"

def test_get_value_plain_text():
    assert body.get_value("plain_text_id") == "test_text"

def test_get_value_static_select():
    assert body.get_value("static_id") == "test_value"
