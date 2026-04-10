class Circle:
    
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, point):
        x1, y1 = point[0], point[1]
        x2, y2 = self.centre[0], self.centre[1]

        dx = x2 - x1
        dy = y2 - y1
        d = float(dx ** 2 + dy ** 2) ** 0.5

        return d < self.radius