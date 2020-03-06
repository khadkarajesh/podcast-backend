class BaseError(Exception):
    def __init__(self, message='', code='', status=''):
        Exception.__init__(self)
        self.message = message
        self.code = code
        self.status = status

    def json(self):
        return {
            'message': self.message,
            'code': self.code,
            'status': self.status
        }
