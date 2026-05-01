"""
Abstracts away the handling of the request body from slack
"""

import json

class Body:
    def __init__(self, body: dict):
        self.body = body

    def get_value(self, value_id):
        """
        the data structure for values is three stages deep with block id, action id and the payload
        """
        if not value_id:
            raise ValueError("Value ID cannot be empty")

        # this level only has the block id
        block_id_level = self.values.get(value_id)
        if not block_id_level:
            raise ValueError(f"No block found for {value_id}")

        # this level only has the action id
        try:
            key = list(block_id_level.keys())[0]
        except IndexError as e:
            raise IndexError("Could not extract the key") from e

        action_id_level = block_id_level.get(key)
        if not action_id_level:
            raise ValueError("Could not get the action_id")

        try:
            vtype = action_id_level["type"]
        except KeyError as e:
            raise ValueError("Could not get the value type") from e

        match vtype:
            case "datepicker":
                return action_id_level["selected_date"]
            case "plain_text_input":
                return action_id_level["value"]
            case "static_select":
                option = action_id_level.get("selected_option")
                if not option:
                    raise ValueError("Could not get the selected option from the static select")
                value = option.get("value")
                if value is None:
                    raise ValueError("Could not get the value from the static select")
                return value
            case _:
                raise ValueError(f"This type is not implemented yet: {vtype}")

    @property
    def view(self):
        return self.body.get("view")

    @property
    def token(self):
        return self.body.get("token")
    
    @property
    def view_id(self):
        return self.body.get("view", {}).get("id")

    @property
    def trigger_id(self):
        return self.body.get("trigger_id", "")

    @property
    def blocks(self) -> list:
        return self.body.get("view", {}).get("blocks")

    @property
    def bot_id(self) -> str:
        return self.body.get("view", {}).get("bot_id")

    @property
    def private_metadata(self) -> dict:
        metadata = self.body.get("view", {}).get("private_metadata")

        if metadata:
            return json.loads(metadata)
        else:
            return {}

    @property
    def team_domain(self) -> str:
        return self.body.get("team", {}).get("domain")

    @property
    def team_id(self) -> str:
        return self.body.get("team", {}).get("id")

    @property
    def user_id(self) -> str:
        return self.body.get("user", {}).get("id")

    @property
    def user_team_id(self) -> str:
        return self.body.get("user", {}).get("team_id")

    @property
    def name(self) -> str:
        return self.body.get("user", {}).get("name")

    @property
    def user_name(self) -> str:
        return self.body.get("user", {}).get("username")

    @property
    def channel_id(self) -> str:
        return self.body.get("channel", {}).get("id")

    @property
    def values(self) -> dict:
        return self.body.get("view", {}).get("state", {}).get("values")

    @property
    def container(self) -> dict:
        return self.body.get("container")

    @property
    def actions(self) -> dict:
        actions = self.body.get("actions")
        return actions[0] if actions else {}

    @property
    def value(self):
        actions = self.body.get("actions")
        return json.loads(actions)[0].get("value") if actions else None

    @property
    def message(self):
        return self.body.get("message")
