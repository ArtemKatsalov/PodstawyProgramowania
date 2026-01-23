class C:
    def __init__(self, sectors):
        # sectors is a dictionary: {sector_letter: number_of_fans}
        self.sectors = sectors

    def m1(self, s, n):
        # change number of fans in sector s
        # or add new sector if it does not exist
        self.sectors[s] = n

    def m2(self, s):
        total = 0

        # go through each character in the string s
        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector]

        return total


# ---- usage example ----
stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

stadium.m1("G", 130)

print(stadium.m2("GD"))   # 280
print(stadium.m2("KEJ"))  # 110
