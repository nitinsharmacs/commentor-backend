class Map(dict):
    def has(self, key) -> bool:
        return list(self.keys()).count(key) > 0
