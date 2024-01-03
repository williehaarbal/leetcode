# 03 jan 2024

class Solution:
    # pylint: skip-file
    
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        return_list = [] # Will hold 2d sublist

        for n in nums:

            # Check for each sublist in the new 2dlist:
            for r in return_list:
                
                # Already in it? Look in another list.
                if n in r:
                    continue
                # Room for number? Place it in it.
                if n not in r:
                    r.append(n)
                    break
            else:
                # New feature learned; if it could't break the loop above, (placed the number),
                # Creat a new sublist and add the number there!
                return_list.append([n])

        return return_list