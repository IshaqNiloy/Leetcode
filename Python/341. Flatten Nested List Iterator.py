# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.list = nestedList
        self.first_attempt = True

    def next(self) -> int:
        i = 0
        # for int
        while True:
            if type(self.list[i]) is int:
                print(self.list[i])
                return self.list[i]
            i += 1

    def hasNext(self) -> bool:
        # for the first iteration no need to pop
        if self.first_attempt:
            self.first_attempt = False
            return True

        # if the list item is an integer
        if type(self.list[0]) is int:
            self.list.pop(0)
        else:
            # if the list item is a list
            self.list[0].pop(0)
            # if the nested list is empty after pop
            if len(self.list[0]) == 0:
                self.list.pop(0)

        return True if len(self.list) > 0 else False


# Your NestedIterator object will be instantiated and called as such:
if __name__ == '__main__':
    nestedList = [1, [4, [6]]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())

    print('v: ', v)

