# 04 jan 2024
# 584 ms execution time

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        chum = {}
        counter = 0
        while(nums):
            x = nums.pop()
            if x in chum:
                chum[x] += 1
            else:
                chum[x] = 1

        for c in chum:
            print(f"Voor waarde: {c}, aantal {chum[c]}")
            x = chum[c]


            if x == 1:
                return -1
            if x == 3 or x == 2:
                counter += 1
                continue
            if x == 4:
                counter += 2
                continue
       
            result = x // 3
            print(f"Counter + {result}")
            counter += result

            x = x - (result * 3)

            if x == 1 or x == 2:
                counter += 1
                print(f"Counter + 1")

        return counter
