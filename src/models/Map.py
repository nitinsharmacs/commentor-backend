class Map(dict):
    """Hash Map"""

    def __init__(self, obj) -> None:
        super().__init__(obj)

    def has(self, key) -> bool:
        """Checks whether map has the key"""
        return list(self.keys()).count(key) > 0
