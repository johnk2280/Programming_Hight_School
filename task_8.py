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

            slot_index = (slot_index + self.step) % len(self.slots)
            if len(cash) == len(self.slots):
                return None

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        slot_index = self.seek_slot(value)
        if slot_index:
            self.slots.append(slot_index)
            return slot_index

        return None

    def find(self, value):
        # находит индекс слота со значением, или None
        return None
