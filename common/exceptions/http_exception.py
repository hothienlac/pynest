


class HttpException(Exception):

    def __init__(self, status, message):
        super().__init__()

        self.status     = status
        self.message    = message


    def get_status(self):
        return self.status
    

    def get_message(self):
        return self.message

