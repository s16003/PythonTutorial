import time


class Timer(object):
    def __init__(self):
        self.start_time = 0

    def __enter__(self):
        self.srart_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapsed time: {0:f} ms'.format(self.millis))