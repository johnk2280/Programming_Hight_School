class PowerSet:

    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def put(self, value):
        if value not in self.storage:
            self.storage.append(value)

    def get(self, value):
        return value in self.storage

    def remove(self, value):
        try:
            self.storage.remove(value)
            return True
        except ValueError:
            return False

    def intersection(self, set2):
        return [el for el in self.storage if el in set2.storage]

    def union(self, set2):
        result = []
        result.extend(self.storage)
        for el in set2.storage:
            if el not in self.storage:
                result.append(el)

        return result

    def difference(self, set2):
        return [el for el in self.storage if el not in set2.storage]

    def issubset(self, set2):
        arr1 = self.storage.copy()
        arr2 = set2.storage.copy()

        return sorted(arr2) == sorted(arr1)[: len(arr2)]
