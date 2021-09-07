class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        result = 0
        for c in str1:
            result = (result * 17 + ord(c)) % self.filter_len

        return 1 << result

    def hash2(self, str1):
        result = 0
        for c in str1:
            result = (result * 223 + ord(c)) % self.filter_len

        return 1 << result

    def add(self, str1):
        self.filter |= self.hash1(str1)
        self.filter |= self.hash2(str1)

    def is_value(self, str1):
        result = self.hash1(str1) + self.hash2(str1)
        return self.filter & result == result
