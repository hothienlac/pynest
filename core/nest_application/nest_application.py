
from pynest.common.services         import Logger


from .nest_application_context      import NestApplicationContext


class NestApplication(NestApplicationContext):

    def __init__(self, container, http_adapter, config, app_options):
        self.logger = Logger('NEST_APPLICATION')
        
