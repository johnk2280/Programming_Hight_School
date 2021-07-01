class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass
