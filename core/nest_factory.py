
from pynest.starlette_platform      import StarletteAdapter

from pynest.common.services         import Logger

from .nest_application              import NestApplication
from .nest_application              import NestApplicationConfig
from .nest_application              import NestApplicationContext


class NestFactoryStatic:

    def __init__(self):
        self.logger = Logger('NEST_FACTORY')


    def create(self, module, app_options):
        http_adapter = StarletteAdapter()

        application_config = NestApplicationConfig()
        