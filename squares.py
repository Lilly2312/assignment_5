class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))
obj = Point(1,3,5)
sum_of_Sq = obj.sqSum()
print("Challenge-1 Output:- \n",sum_of_Sq)