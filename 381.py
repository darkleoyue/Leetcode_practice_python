class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.List = []
        self.Dict = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.List.append(val)
        res = val not in self.Dict.keys()
        if res:
            self.Dict[val] = {len(self.List) - 1}
        else:
            self.Dict[val].add(len(self.List) - 1)
        return res


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        res = val in self.Dict.keys()
        if res:
            index_val = self.Dict[val].pop()
            index_end = len(self.List) - 1
            last_val = self.List[index_end]
            self.List[index_val] = self.List[index_end]
            if index_end != index_val:
                self.Dict[last_val].remove(index_end)
                self.Dict[last_val].add(index_val)
            if not len(self.Dict[val]):
                self.Dict.pop(val)
            self.List.pop()
        return res

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.List)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
