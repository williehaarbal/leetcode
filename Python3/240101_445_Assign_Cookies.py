class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # If there are no cookies or no childern, you cannot satisfy the childern. (Which sounds ow so wrong btw)
        if len(s) == 0:
            return 0
        if len(g) == 0:
            return 0
        
        # The idea is that we give the kids with the smallest satisfy score the smallest possible cookie;
        # I suggest we sort both cookies and children greed factor from low to highest.

        kid = sorted(g)
        cookie = sorted(s)

        # We take the the kiddo with the smallest kid; and keep grabbing the smallest cookie till (s)he is satisfied.

        satisfied_kids = 0

        for k in kid:
            if not cookie:
                return satisfied_kids

            satisfied = False

            # Keep popping cookies until kid is satisfied.
            # Also check if there are still cookies left over.
            while(not satisfied and cookie):

                smallest_cookie = cookie.pop(0)

                # If cookie is big enough, we increment the counter, and we break the loop.
                if smallest_cookie >= k:
                    satisfied = True
                    satisfied_kids += 1 
        
        return satisfied_kids