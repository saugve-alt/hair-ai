class SessionState:
    def __init__(self):
        self.data = {}
        self.finished = False

    # -------- DATA --------
    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def has(self, key):
        return key in self.data

    # -------- SESSION --------
    def finish(self):
        self.finished = True

    def is_finished(self):
        return self.finished

    # -------- EXPORT --------
    def dump(self):
        return {
            "finished": self.finished,
            "data": self.data
        }
