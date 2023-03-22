class Map(dict):
    """Hash Map"""

    def has(self, key) -> bool:
        """Checks whether map has the key"""
        return list(self.keys()).count(key) > 0
