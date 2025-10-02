class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        try:
            bottles_drunk = numBottles
            empty_bottles = numBottles
            full_bottles = 0

            while True:
                while True:
                  if empty_bottles >= numExchange:
                    empty_bottles -= numExchange
                    numExchange += 1 
                    full_bottles += 1
                  else: 
                     break
                bottles_drunk += full_bottles
                empty_bottles += full_bottles
                full_bottles = 0

                if empty_bottles < numExchange:
                  break

            return bottles_drunk
        except Exception as e:
            print(e)

if __name__ == '__main__':
    obj = Solution()
    print(obj.maxBottlesDrunk(13, 6))