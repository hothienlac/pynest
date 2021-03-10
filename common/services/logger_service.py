import datetime


LOG_LEVEL = [
    'log',
    'error',
    'warn',
    'debug',
    'verbose',
]

class Logger:

    def __init__(self, context='NEST_GLOBAL', timestamp=True):
        self.timestamp  = timestamp
        self.context    = context

        self.debug      = lambda message: self.print('debug'    , message)
        self.verbose    = lambda message: self.print('verbose'  , message)
        self.log        = lambda message: self.print('log'      , message)
        self.warn       = lambda message: self.print('warn'     , message)
        self.error      = lambda message: self.print('error'    , message)


    def print(self, level, message):
        if level in LOG_LEVEL:
            time = f'[{str(datetime.datetime.now())}]\t' if self.timestamp else ''
            print(f'{time}[{self.context}]\t[{level}]\t:\t{message}')
