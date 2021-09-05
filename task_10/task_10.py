class PowerSet:

    def __init__(self):
        self.slots = []

    def size(self):
        return len(self.slots)

    def put(self, value):
        if value not in self.slots:
            self.slots.append(value)

    def get(self, value):
        return value in self.slots

    def remove(self, value):
        try:
            self.slots.remove(value)
            return True
        except ValueError:
            return False

    def intersection(self, set2):
        result = PowerSet()
        for value in self.slots:
            if set2.get(value):
                result.put(value)

        return result

    def union(self, set2):
        result = PowerSet()
        result.slots = self.slots.copy()
        for el in set2.slots:
            if el not in result.slots:
                result.put(el)

        return result

    def difference(self, set2):
        result = PowerSet()
        for value in self.slots:
            if value not in set2.slots:
                result.put(value)

        return result

    def issubset(self, set2):
        arr1 = self.slots.copy()
        arr2 = set2.slots.copy()

        return sorted(arr2) == sorted(arr1)[: len(arr2)]
