class Format():

    def __init__(self, file_, pretty=False):
        self.file = file_
        self.pretty = pretty

    def read(self):
        raise NotImplementedError

    def write(self, data):
        raise NotImplementedError
