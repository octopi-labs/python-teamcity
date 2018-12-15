class TCException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __repr__(self):
        return "{0}: message={1}".format(self.status_code, self.message)