"""
Abstracts away the handling of the request event from slack
"""

class Event:
    def __init__(self, event):
        self.event = event

    @property
    def type(self):
        return self.event.get("type")

    @property
    def user_id(self):
        return self.event.get("user")

    @property
    def channel(self):
        return self.event.get("channel")

    @property
    def event_ts(self):
        return self.event.get("event_ts")

    @property
    def thread_ts(self):
        return self.event.get("thread_ts")

    @property
    def text(self):
        return self.event.get("text")

    @property
    def tab(self):
        return self.event.get("tab")

    @property
    def team(self):
        return self.event.get("view", {}).get("team")

    @property
    def team_id(self):
        return self.event.get("view", {}).get("team_id")

    @property
    def app_id(self):
        return self.event.get("view", {}).get("app_id")

    @property
    def metadata(self):
        return self.event.get("view", {}).get("private_metadata")
