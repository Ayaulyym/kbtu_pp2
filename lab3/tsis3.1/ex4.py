class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Coordinates(self):
        print(self.x, self.y)
    def Change(self, x0, y0):
        self.x = x0
        self.y = y0
    def Distance(self):
        print((self.x**2 + self.y**2)**0.5)
        