import random


class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        else:
            self.vals.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            self.vals.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_val = random.choice(tuple(self.vals))
        return random_val


if __name__ == "__main__":
    # Your RandomizedSet object will be instantiated and called as such:
    val = 1
    obj = RandomizedSet()
    param_1 = obj.insert(val)
    param_2 = obj.insert(2)
    param_3 = obj.remove(val)
    param_4 = obj.getRandom()
    print(param_1)
    print(param_2)
    print(param_4)
    print(obj.vals)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()