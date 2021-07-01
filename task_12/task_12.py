class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        slot_index = self.hash_fun(key)
        for i in range(self.size):
            if not self.slots[slot_index] or self.slots[slot_index] == key:
                self.slots[slot_index] = key
                self.values[slot_index] = value
                self.hits[slot_index] += 1
                break
            slot_index = (slot_index + 4) % self.size

        self.displace(key, value)

    def get(self, key):
        try:
            slot_index = self.slots.index(key)
            self.hits[slot_index] += 1
            return self.values[slot_index]
        except ValueError:
            return

    def displace(self, new_key, new_value):
        slot_index = self.hits.index(min(self.hits))
        self.slots[slot_index] = new_key
        self.values[slot_index] = new_value
        self.hits[slot_index] = 1
