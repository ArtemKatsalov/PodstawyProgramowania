class C:
    def __init__(self, points):
        # points is a 2D array: list of [x, y]
        self.points = points

    def m(self, n):
        count = 0

        # go through all points
        for point in self.points:
            x = point[0]
            y = point[1]

            # check if the point is in the first quadrant
            if x > 0 and y > 0:
                count += 1

        # check if at least n points are in the first quadrant
        if count >= n:
            return True
        else:
            return False


# ---- usage ----
obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

print(obj.m(2))  # True
print(obj.m(3))  # False
