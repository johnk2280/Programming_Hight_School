class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.storage = [0] * self.filter_len

    def hash1(self, str1):
        result = 0
        for c in str1:
            result = (result * 17 + ord(c)) % self.filter_len

        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            result = (result * 223 + ord(c)) % self.filter_len

        return result

    def add(self, str1):
        self.storage[self.hash1(str1)] = 1
        self.storage[self.hash2(str1)] = 1

    def is_value(self, str1):
        return False if self.storage[self.hash1(str1)] == 0 or self.storage[self.hash2(str1)] == 0 else True
