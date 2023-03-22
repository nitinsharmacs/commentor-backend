class Array(list):
    """List with features of javascript array"""

    def unshift(self, item) -> int:
        """Insert item in list top"""
        self.insert(0, item)
        return len(self)
