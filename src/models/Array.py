class Array(list):
    def unshift(self, item) -> int:
        self.insert(0, item)
        return len(self)
