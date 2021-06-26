class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        cash = []
        slot_index = self.hash_fun(key)
        while True:
            if slot_index not in cash:
                cash.append(slot_index)

            if self.slots[slot_index] == key:
                return True

            if len(cash) == self.size:
                return None

            slot_index = (slot_index + 4) % self.size

    def put(self, key, value):
        cash = []
        slot_index = self.hash_fun(key)
        while True:
            if slot_index not in cash:
                cash.append(slot_index)

            if self.slots[slot_index] == key or not self.slots[slot_index]:
                self.values[slot_index] = value
                self.slots[slot_index] = key
                break

            if len(cash) == self.size:
                break

            slot_index = (slot_index + 4) % self.size

    def get(self, key):
        if self.is_key(key):
            cash = []
            slot_index = self.hash_fun(key)
            while True:
                if slot_index not in cash:
                    cash.append(slot_index)

                if self.slots[slot_index] == key:
                    return self.values[slot_index]

                if len(cash) == self.size:
                    return None

                slot_index = (slot_index + 4) % self.size
