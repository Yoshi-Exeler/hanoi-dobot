class Vector:
    X: float
    Y: float
    Z: float

    def __init__(self,x,y,z) -> None:
        self.X = x
        self.Y = y
        self.Z = z
        pass

    def __str__(self) -> str:
        return "X:"+str(self.X)+"Y:"+str(self.Y)+"Z:"+str(self.Z)
        pass