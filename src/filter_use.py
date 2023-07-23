class FilterUse:
    """
    filter 使用
    """
    def __init__(self, list1) -> None:
        self.list1 = list1
    def filter_use(self, func):
        """
        Executes the filter function on two lists.
 
        Args:
            func: A function that will be applied to elements of two lists.
 
        Returns:
            A filter object containing the results of applying the function to the elements of the two lists.
        """
        return filter(func, self.list1)
    

f = FilterUse([1, 2, 3])

print(list(f.filter_use(lambda x: x % 2 == 0)))