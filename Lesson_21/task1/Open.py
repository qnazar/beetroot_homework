"""Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method, which has to cover all the requirements to context managers"""
import logging
from logging import FileHandler, Formatter


class Open:

    __counter = 0

    @staticmethod
    def create_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = FileHandler(filename=f'logs_{__name__}.txt')
        handler.setFormatter(Formatter('[%(asctime)s: %(levelname)s in %(funcName)s] %(message)s'))
        logger.addHandler(handler)
        return logger

    logger = create_logger()

    @classmethod
    def get_counter(cls):
        return cls.__counter

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.logger.debug('Instance of context manager has been created in {} mode'.format(self.mode))
        Open.__counter += 1
        self.logger.info(f'Total count of instances - {Open.get_counter()}')

    def __enter__(self):
        self.logger.debug('__enter__ method starts')
        self.file = open(self.filename, self.mode)
        self.logger.debug('File opened')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.debug('__exit__ method starts')
        self.file.close()
        self.logger.info(f'File closed - {self.file.closed}')
        if exc_type:
            self.logger.warning(msg=f'Error occurred in the body of manager: {exc_type} - {exc_val}')
            return True


# with Open('file.txt', 'w') as f:
#     f.write('test')
#
#
# with Open('file.txt', 'r') as f:
#     data = f.read()
#
# with Open('file.txt', 'a') as f:
#     f.write('appending')
#
# with Open('file.txt', 'r') as f:
#     data = f.read()
#     print(int(data))
#
# with Open('not_exist.txt') as f:
#     f.read()
