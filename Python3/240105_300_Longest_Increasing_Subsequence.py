# This one is so hard, I still haven't figured it out...

# Gonna try again tomorrow.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = len(nums)
        longest_sub_list = [1] * length

        for sub in range(0, length):
            sublist = nums[sub:length]


            print(f'Working with {sublist}')
            print(f'Counter: {sub}')
            chum = []
            
            chum.append(sublist.pop(0))
            while sublist:
                print(f'Chum: {chum}')
                print(f'Sublist: {sublist}')
                next = sublist.pop(0)
                print(f'next: {next}')

                if next > chum[-1]:
                    print(f"added {next}")
                    chum.append(next)
                    print(f'Why error here: {chum}')
                    continue

                if len(chum) >= 2 and next < chum[-1] and next > chum[-2]:
                    print(f"Replaced last with {next}")
                    chum[-1] = next
            else:
                print(f'After else {chum}')
                print(f'After else length {len(chum)}')
                longest_sub_list[sub] = len(chum)
                print(f' results: {longest_sub_list}')

        return max(longest_sub_list)