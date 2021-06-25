class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode('utf-8')) % self.size

    def seek_slot(self, value):
        cash = set()
        slot_index = self.hash_fun(value)
        while True:
            cash.add(slot_index)
            if not self.slots[slot_index]:
                return slot_index

            slot_index = (slot_index + self.step) % self.size
            if len(cash) == len(self.slots):
                return None

    def put(self, value):
        slot_index = self.seek_slot(value)
        if slot_index or slot_index == 0:
            self.slots[slot_index] = value
            return slot_index

        return None

    def find(self, value):
        cash = set()
        slot_index = self.hash_fun(value)
        while True:
            cash.add(slot_index)
            if self.slots[slot_index] == value:
                return slot_index

            slot_index = (slot_index + self.step) % self.size
            if len(cash) == self.size:
                return None
