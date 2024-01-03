# 03 jan 2024

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # It doesn't really matter how many "empty" grids there are in a row (and where), just how many there are on a row.
        # Also if there are 0 lasers on a row, it can basicly get ignored.
        # Below we count per row, how many lasers there are and make an array with rows.
        chum = []

        for b in bank:
            x = b.count('1')
            if x != 0:
                chum.append(x)

        # If previous line had 3 lasers, and the next line has 2 lasers it will have (2 * 3) = 6 lasers.
        # We do that for every row.
        prev = 0
        total = 0
        for c in chum:
            total += (prev * c)
            prev = c

        return total
