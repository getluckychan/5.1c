class Overloads:
    def __init__(self, x):
        self.x = x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * float(other.x)

    def __str__(self):
        pass
