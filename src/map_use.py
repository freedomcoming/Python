class MapUse:
    """
    map 使用
    """
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        self.list2 = list2

    def map_use(self, func):
        """
        Executes the map function on two lists.

        Args:
            func: A function that will be applied to elements of two lists.

        Returns:
            A map object containing the results of applying the function to the elements of the two lists.
        """
        return map(func, self.list1, self.list2)


m = MapUse([1, 2, 3], [4, 5, 6])

print(list(m.map_use(lambda x, y: (x,y))))
