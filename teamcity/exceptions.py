class TCException(Exception):
    def __init__(self, status_code, reason, message):
        self.status_code = status_code
        self.reason = reason
        self.message = message

    def __repr__(self):
        return self.reason or self.message