




class NestContainer:

    def __init__(self, application_config):
        self.global_modules = set()


        self.application_config = application_config


    def get_application_config(self):
        return self.application_config


    def set_http_adapter(self, http_adapter):
        pass

