class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        Area = uniform(0, pi * self.r * self.r)
        R = sqrt(Area/pi)
        theta = uniform(0, 2*pi)
        return [self.x + cos(theta) * R, self.y + sin(theta) * R]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
