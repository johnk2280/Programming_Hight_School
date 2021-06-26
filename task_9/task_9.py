class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        slot_index = self.hash_fun(key)
        # возвращает True если ключ имеется,
        # иначе False
        return True if self.slots[slot_index] else False

    def put(self, key, value):
        pass
        # гарантированно записываем
        # значение value по ключу key

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        return None
